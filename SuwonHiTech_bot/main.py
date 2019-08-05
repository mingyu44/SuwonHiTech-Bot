# import modules
import logging
from today_food import *
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, )

# enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
# my bot token from BotFather
token = '842980380:AAFI7nTXGfCnnf3t9dTPvwhSw6i6BTytMz0'

# start command handler
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="봇 작동합니다.")

# wrong command handler
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="잘못된 명령어입니다.")

# define main
def main():
    # Create Updater object and attach dispatcher to it
    updater = Updater(token)
    dp = updater.dispatcher
    print("Bot started")

    # Start the bot
    updater.start_polling()
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('그제', the_day_before_yesterday_food_list))
    dp.add_handler(CommandHandler('어제', yesterday_food_list))
    dp.add_handler(CommandHandler('오늘', today_food_list))
    dp.add_handler(CommandHandler('내일', tomorrow_food_list))
    dp.add_handler(CommandHandler('모레', the_day_after_tomorrow_food_list))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Run the bot until you press Ctrl-C
    updater.idle()
    updater.stop()

if __name__ == '__main__':
    main()