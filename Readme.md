# Discord News Bot

**`Version: 1.0`**

This is a Discord Bot that specializes in displaying the current news globally. The bot will give the information after the user uses the correct command prefix followed by the command name.

**Additonal information: See the [Discord Documentation](https://discordpy.readthedocs.io/en/stable/) for detailed instructions.**

## Features

- Clears the messages between multiple people or the bot itself in the channel
- Greets the user when the bot is successfully turned on
- Outputs general information about the bot
- Outputs three types of news globally or gaming related
- Connects to the mySQL database to fetch news (WIP due to Discord API)

## Setup

**Note: It's advised to setup a Virtual Environment to avoid package issues between the system if multiple projects exist.**

1. Go to the project's directory:
```bash
cd "your folder name"
python -m venv "environment name of choice"
```

2. Activate the Virtual Environment:
```bash
Linux: source env/bin/activate
Windows: env\Scripts\activate.bat

# to deactive type deactive while in the venv
```

3. Install python packages:
```bash
pip install discord
pip install MySQLdb
```
## Create the Discord Bot on Discord's Developer page

Refer to [this page](https://discordpy.readthedocs.io/en/stable/discord.html) in the Discord Documentation. After that, have fun and get creative with your newly created bot!

**Additional information: See [this page](https://discordpy.readthedocs.io/en/stable/ext/commands/index.html) for commands and [this page](https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html) for tasks.**

## MySQL Instructions:

Coming soon: This will be a detailed process for everyone to fully understand.