
import os
from telegram import Bot
from telegram.error import InvalidToken

# Read token
token = os.getenv("TELEGRAM_BOT_TOKEN")

# Sanity check output
print(f"Read TELEGRAM_BOT_TOKEN: {token[:8]}... (length: {len(token) if token else 0})")

# Try creating the bot
try:
    bot = Bot(token=token)
    print("Bot initialized successfully.")
except InvalidToken:
    print("ERROR: Invalid token — check environment variable spelling and value.")
