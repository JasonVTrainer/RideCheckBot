
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

async def ridecheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚵‍♂️ RideCheck – Sublett Creek / Rush Creek\n"
        "- Last Rainfall: May 6 (1.5\")\n"
        "- Adjusted Drying Time: 6.6 days\n"
        "- Ride-Ready Date: May 13\n"
        "- Days Remaining: 0.6\n"
        "- Rideable Window: May 13–15\n"
        "- Next Rain: May 16 (40%)\n"
        "- Weather: 83°F, 38% humidity, 7 mph wind"
    )

async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("may_chart.png", "rb") as photo:
        await update.message.reply_photo(photo)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("ridecheck", ridecheck))
    app.add_handler(CommandHandler("chart", chart))
    logger.info("Bot started")
    app.run_polling()

if __name__ == "__main__":
    main()
