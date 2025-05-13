
import os
from flask import Flask
from telegram import Bot
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("BOT_CHAT_ID")

@app.route("/forecast", methods=["GET"])
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
        return "Forecast sent!", 200
    return "CHAT_ID not set", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
