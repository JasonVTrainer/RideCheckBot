
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_ACTIVE = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("RideCheck activated!")

async def ridecheck(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Daily forecast: trail info goes here.")

def main():
    global BOT_ACTIVE
    if BOT_ACTIVE:
        return
    BOT_ACTIVE = True

    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN not set in environment variables")

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ridecheck", ridecheck))

    application.run_polling()

if __name__ == "__main__":
    main()
