from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from math import trunc
from psutil._common import bytes2human
import psutil
import time
import datetime
import logging

#setup logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#read API-token
file = open('api_token.txt')
API_TOKEN = file.readline().rstrip('\n');
file.close()

#reply with uptime of system
def uptime(update,context):
    seconds_elapsed = time.time() - psutil.boot_time()
    hours=trunc(seconds_elapsed//3600)
    minutes=trunc((seconds_elapsed//60)%60)
    update.message.reply_text(str(hours)+"h"+str(minutes)+"m")

#reply with diskusage
def diskusage(update,context):
    disk_usage = psutil.disk_usage('/')
    used=bytes2human(disk_usage.used)
    total=bytes2human(disk_usage.total)
    update.message.reply_text(used+" / "+total+" used")

#start bot and poll for user input
def main():
    updater = Updater(API_TOKEN,use_context=True)

    dispatcher = updater.dispatcher

    #add commandHandlers here:
    dispatcher.add_handler(CommandHandler("uptime",uptime))
    dispatcher.add_handler(CommandHandler("diskusage",diskusage))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
