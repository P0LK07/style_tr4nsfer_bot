import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.bot import Bot
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)

def SUfunc(some_photo):
    """Working with CycleGAN"""
    return some_photo

def start(update, context):
    update.message.reply_text('Welcome to Xbot!  ~(^o^)~ \nSend me photo and in a few seconds I will show you 3d implementation of it')

def help(update, context):
    update.message.reply_text('All I can is transfer 2d photos to 3d sketch. So send me photo ( ͡❛ -͡❛ )')

def reply(update, context):
    update.message.reply_text("Here is your 3d photo:")
    kek = bytes(bot.get_file(update.message.photo[2]["file_id"]).download_as_bytearray())
    print(kek)
    update.message.reply_photo(SUfunc(kek))

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.document.image, reply))
    dp.add_handler(MessageHandler(Filters.photo, reply))

    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN, webhook_url='https://style-tr4nsfer-bot.herokuapp.com/'+TOKEN)
    updater.bot.setWebhook('https://style-tr4nsfer-bot.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
