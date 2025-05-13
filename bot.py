import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
print(f"TOKEN from env: {repr(TOKEN)}")  # DEBUG

async def ridecheck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Drying forecast: wind 12mph, humidity 55%")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("ridecheck", ridecheck))

if __name__ == "__main__":
    app.run_polling()
