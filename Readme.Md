# Discord Bot - Currency Converter and Timezone Information

This is a simple Discord bot built using discord.py that provides currency conversion and timezone information.

## Features

- Currency conversion from Indonesian Rupiah (IDR) to other currencies (USD, RUB, BRL, KRW).
- Displaying current time in different timezones (England, Russia, Dubai, Korea).
- Joining and leaving voice channels.

## Requirements

- Python 3.7 or higher
- discord.py 1.7.3
- pytz 2021.3
- requests 2.26.0

## Installation

1. Navigate to the project directory:
```sh
cd discord-bot
```
2. Install required dependencies:
```sh
pip install -r requirements.txt
```
3. Create a new Discord bot and get the token from the Discord Developer Portal.
4. Replace 'YOUR_DISCORD_BOT_TOKEN' in the bot.py file with your bot token.
5. Run the bot:
```sh
python bot.py
```
## Usage
- Use the !convert command to convert currency. Example: !convert 100000 IDR USD.
- Use the !time command to display the current time in a specific timezone. Example: !time inggris.
- Use the !join command to make the bot join a voice channel.
- Use the !leave command to make the bot leave a voice channel.
