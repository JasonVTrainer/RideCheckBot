
import os
from datetime import datetime
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("BOT_CHAT_ID")  # optional for cron use

async def ridecheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "🚵‍♂️ RideCheck – Sublett Creek / Rush Creek\n"
        "- Last Rainfall: May 6 (1.5\")\n"
        "- Adjusted Drying Time: 6.6 days\n"
        "- Ride-Ready Date: Tue, May 13\n"
        "- Days Remaining: 0.6\n"
        "- Rideable Window: May 13–15\n"
        "- Next Rain: May 16 (40%)\n"
        "- Today’s Weather: 83°F, 38% humidity, 7 mph wind"
    )
    await update.message.reply_text(message)

async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("may_chart.png", "rb") as photo:
        await update.message.reply_photo(photo)

def send_forecast():
    bot = Bot(token=TOKEN)
    message = (
        "🚵‍♂️ RideCheck – Sublett Creek / Rush Creek\n"
        "- Last Rainfall: May 6 (1.5\")\n"
        "- Adjusted Drying Time: 6.6 days\n"
        "- Ride-Ready Date: Tue, May 13\n"
        "- Days Remaining: 0.6\n"
        "- Rideable Window: May 13–15\n"
        "- Next Rain: May 16 (40%)\n"
        "- Today’s Weather: 83°F, 38% humidity, 7 mph wind"
    )
    if CHAT_ID:
        bot.send_message(chat_id=CHAT_ID, text=message)
        with open("may_chart.png", "rb") as photo:
            bot.send_photo(chat_id=CHAT_ID, photo=photo)

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "send_forecast":
        send_forecast()
        return

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("ridecheck", ridecheck))
    app.add_handler(CommandHandler("chart", chart))
    logger.info("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
