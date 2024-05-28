from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import os
from core.settings import TELEGRAM_TOKEN

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_BOT_TOKEN = TELEGRAM_TOKEN

def start(update, context):
    update.message.reply_text('Welcome to the URL Shortener Bot! Send me a URL to shorten.')

def shorten(update, context):
    long_url = update.message.text
    response = requests.post('http://127.0.0.1:8000/create_short_url/', json={'original_url': long_url})
    if response.status_code == 200:
        short_url = response.json().get('short_url')
        update.message.reply_text(f'Shortened URL: {short_url}')
    else:
        update.message.reply_text('Failed to shorten URL. Please try again.')

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, shorten))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()