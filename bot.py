
import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_CHAT_ID = os.getenv("BOT_CHAT_ID")
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# Telegram Command Handler
async def ridecheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="RideCheck activated!")

# Flask route to send forecast
@app.route('/forecast', methods=['GET'])
def send_forecast():
    try:
        bot = Bot(token=BOT_TOKEN)
        bot.send_message(chat_id=BOT_CHAT_ID, text="Daily forecast: trail info goes here.")
        img_path = "may_chart.png"
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                bot.send_photo(chat_id=BOT_CHAT_ID, photo=f)
        else:
            logging.warning("Chart image missing.")
        return "Forecast sent!"
    except Exception as e:
        logging.error(f"Forecast error: {e}")
        return "Error", 500

def run_flask():
    app.run(host='0.0.0.0', port=10000)

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("ridecheck", ridecheck))
    logging.info("Starting bot polling...")
    app.run_polling()

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    run_bot()
