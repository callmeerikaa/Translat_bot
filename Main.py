from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from googletrans import Translator

translator = Translator()

async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    translation = translator.translate(text, src='en', dest='fa')
    await update.message.reply_text(f"🔁 ترجمه:\n{translation.text}")

TOKEN = "8417537253:AAGpr8btG-m7ojZtYKLxtb40jEgIb0OWzTY"

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))

print("🤖 ربات در حال اجراست...")
app.run_polling()
