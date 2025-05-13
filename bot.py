import os
from flask import Flask
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("BOT_CHAT_ID")

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

async def ridecheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("RideCheckBot is online and ready.")

@app.route("/forecast", methods=["GET"])
def forecast():
    try:
        bot.send_message(chat_id=CHAT_ID, text="RideCheck Forecast:\n- Trails dry in 2.5 days.\n- Wind: 14mph\n- Humidity: 53%")
        with open("may_chart.png", "rb") as chart:
            bot.send_photo(chat_id=CHAT_ID, photo=chart)
        return "Forecast sent!"
    except Exception as e:
        print(f"Error sending forecast: {e}")
        return "Failed to send forecast."

def start_polling():
    telegram_app = Application.builder().token(BOT_TOKEN).build()
    telegram_app.add_handler(CommandHandler("ridecheck", ridecheck))
    telegram_app.run_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=start_polling).start()
    app.run(host="0.0.0.0", port=10000)