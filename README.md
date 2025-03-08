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

This project is licensed under the MIT License - see the details below:

```
MIT License

Copyright (c) 2025 PREM-O7

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
