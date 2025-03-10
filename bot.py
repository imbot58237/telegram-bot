from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# টেলিগ্রাম বট টোকেন
BOT_TOKEN = "7887571273:AAG5YixqdDOoWljVUG0AZRm1bmzuWLOfrlw"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("হ্যালো! আমি তোমার বট।")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("তুমি `/start` দিয়ে শুরু করতে পারো!")

async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    await update.message.reply_text(f"তুমি লিখেছো: {text}")

async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("বট চালু হয়েছে...")
    await app.run_polling()

import asyncio
asyncio.run(main())