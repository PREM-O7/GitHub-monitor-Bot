import discord
from discord.ext import commands, tasks
import aiohttp
import sqlite3

# Initialize Discord bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Database setup
conn = sqlite3.connect('github_monitor.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS config
             (guild_id INTEGER PRIMARY KEY, channel_id INTEGER, github_username TEXT, last_commit_sha TEXT, last_repo_id INTEGER)''')
conn.commit()

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com"

# Reusable HTTP session
session = aiohttp.ClientSession()

# Function to fetch latest commit from a GitHub profile
async def fetch_latest_commit(username):
    url = f"{GITHUB_API_URL}/users/{username}/events/public"
    async with session.get(url) as response:
        if response.status == 200:
            events = await response.json()
            for event in sorted(events, key=lambda e: e.get('created_at', ''), reverse=True):
                if event['type'] == 'PushEvent':
                    commit = event['payload']['commits'][-1]
                    repo_name = event['repo']['name']
                    commit_url = f"https://github.com/{repo_name}/commit/{commit['sha']}"
                    return commit, repo_name, commit_url
        return None, None, None

# Function to fetch latest repository from a GitHub profile
async def fetch_latest_repo(username):
    url = f"{GITHUB_API_URL}/users/{username}/repos?sort=created"
    async with session.get(url) as response:
        if response.status == 200:
            repos = await response.json()
            if repos:
                return repos[0]
    return None

# Background task to check for updates
@tasks.loop(minutes=5)
async def check_for_updates():
    for guild in bot.guilds:
        c.execute("SELECT channel_id, github_username, last_commit_sha, last_repo_id FROM config WHERE guild_id = ?", (guild.id,))
        row = c.fetchone()
        if row:
            channel_id, github_username, last_commit_sha, last_repo_id = row
            channel = bot.get_channel(channel_id)
            if channel:
                # Check for new commits
                latest_commit, repo_name, commit_url = await fetch_latest_commit(github_username)
                if latest_commit and latest_commit['sha'] != last_commit_sha:
                    c.execute("UPDATE config SET last_commit_sha = ? WHERE guild_id = ?", (latest_commit['sha'], guild.id))
                    conn.commit()
                    await channel.send(f"**New Commit by {github_username}**\n"
                                       f"Repository: {repo_name}\n"
                                       f"Message: {latest_commit['message']}\n"
                                       f"URL: {commit_url}")

                # Check for new repositories
                latest_repo = await fetch_latest_repo(github_username)
                if latest_repo and latest_repo['id'] != last_repo_id:
                    c.execute("UPDATE config SET last_repo_id = ? WHERE guild_id = ?", (latest_repo['id'], guild.id))
                    conn.commit()
                    await channel.send(f"**New Repository Created by {github_username}**\n"
                                       f"Name: {latest_repo['name']}\n"
                                       f"Description: {latest_repo['description']}\n"
                                       f"URL: {latest_repo['html_url']}")

# Command to enable GitHub updates
@bot.command(name="enable_github_updates")
async def enable_github_updates(ctx, github_username: str):
    c.execute("INSERT OR REPLACE INTO config (guild_id, channel_id, github_username) VALUES (?, ?, ?)", 
              (ctx.guild.id, ctx.channel.id, github_username))
    conn.commit()
    await ctx.send(f"GitHub updates enabled for {github_username}.")

# Command to disable GitHub updates
@bot.command(name="disable_github_updates")
async def disable_github_updates(ctx):
    c.execute("DELETE FROM config WHERE guild_id = ?", (ctx.guild.id,))
    conn.commit()
    await ctx.send("GitHub updates disabled.")

# Start the bot
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    check_for_updates.start()

@bot.event
async def on_close():
    await session.close()
    conn.close()

# Run the bot
bot.run("YOUR_DISCORD_BOT_TOKEN")
