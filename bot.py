
import os
import logging
import subprocess
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    import telegram
    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
except ModuleNotFoundError as e:
    logger.error("Module 'telegram' not found. Printing installed packages:")
    subprocess.run([sys.executable, "-m", "pip", "freeze"])
    raise e

TOKEN = os.getenv("BOT_TOKEN")

async def ridecheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚵‍♂️ RideCheck Debug\n"
        "- Telegram module loaded successfully.\n"
        "- Bot is working."
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("ridecheck", ridecheck))
    logger.info("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
