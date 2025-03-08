# GitHub Monitor Discord Bot

A Discord bot that monitors a GitHub profile for new commits and repositories, then posts updates in a designated channel.

## Features
✔️ Monitors a GitHub profile for **new commits** and **repository creations**.  
✔️ Sends updates in the **configured Discord channel**.  
✔️ Uses an SQLite database for **persistent tracking**.  
✔️ Supports commands to enable/disable tracking and set the update channel.  
✔️ Checks GitHub every **5 minutes**.  

## Installation

1. **Clone the Repository:**  
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/github-monitor-bot.git
   cd github-monitor-bot
   ```

2. **Install Dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up the Bot Token:**  
   - Open `github_monitor_bot.py` and replace `"YOUR_DISCORD_BOT_TOKEN"` with your actual bot token.  

4. **Run the Bot:**  
   ```sh
   python github_monitor_bot.py
   ```

## Commands  

| Command | Description |
|---------|------------|
| `!enable_github_updates <GitHub_Username>` | Enables GitHub tracking for a user |
| `!disable_github_updates` | Disables GitHub tracking |
| `!set_github_channel <#channel>` | Sets the channel for updates |

## Example Usage

1. **Enable GitHub updates:**  
   ```
   !enable_github_updates PREM-O7
   ```
2. **Set a specific channel for updates:**  
   ```
   !set_github_channel #github-updates
   ```

## License

This project is licensed under the MIT License
