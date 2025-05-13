import os
from flask import Flask
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("BOT_CHAT_ID")

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

async def ridecheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Received /ridecheck command")
    await update.message.reply_text("RideCheckBot is online and responding!")

@app.route("/forecast", methods=["GET"])
def forecast():
    logger.info("Received /forecast web request")
    try:
        bot.send_message(chat_id=CHAT_ID, text="RideCheck Forecast:\n- Trails dry in 2.5 days.\n- Wind: 14mph\n- Humidity: 53%")
        logger.info("Forecast text sent.")
        if os.path.exists("may_chart.png"):
            with open("may_chart.png", "rb") as chart:
                bot.send_photo(chat_id=CHAT_ID, photo=chart)
            logger.info("Chart image sent.")
        else:
            logger.warning("may_chart.png not found!")
        return "Forecast sent!"
    except Exception as e:
        logger.error(f"Error sending forecast: {e}")
        return "Failed to send forecast."

def start_polling():
    logger.info("Starting Telegram polling...")
    telegram_app = Application.builder().token(BOT_TOKEN).build()
    telegram_app.add_handler(CommandHandler("ridecheck", ridecheck))
    telegram_app.run_polling()

if __name__ == "__main__":
    logger.info("Launching RideCheckBot...")
    import threading
    threading.Thread(target=start_polling).start()
    app.run(host="0.0.0.0", port=10000)