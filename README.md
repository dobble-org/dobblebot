# Dobblebot
A Telegram bot to help you detect Dobble icons on cards.

![](https://github.com/dobble-org/dobblebot/blob/main/imgs/example.gif)

# How to start the bot on ubuntu 
1. Clone the repository
   ```bash
   git clone https://github.com/dobble-org/dobblebot.git
   cd dobblebot
   git submodule update --init
   ```
1. Create a virtual environment
   ```bash
   python3 -m pip install virtualenv
   python3 -m virtualenv venv
   source ./venv/bin/activate
   ```
1. Install dependencies
   ```bash
   python -m pip install -r requirements.txt
   ```
1. Install system dependencies
   ```bash
   sudo apt install -y ffmpeg libsm6 libxext6 
   ```
1. Set a Telegram bot token to environment 
   ```bash
   export TELEGRAM_BOT_TOKEN=...
   ```
1. Setup additional environment variables:
   ```bash
   source .env
   ```
1. Run the bot 
   ```bash
   python \cli/bot.py
   ```
