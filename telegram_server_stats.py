#telegram_server_stats.py
####################################################################
#entry point of the bot
#
#reads in API_TOKEN and sets up bot. Also adds all used command_blocks
####################################################################

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from threading import Thread
import command_blocks as cmd
import filesystem_monitoring as fmonitor
import configuration as config

#setup logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#read API-token
API_TOKEN = config.get_API_TOKEN()

#start bot and poll for user input
def main():
    updater = Updater(API_TOKEN,use_context=True)

    dispatcher = updater.dispatcher

    #add commandHandlers here:
    dispatcher.add_handler(CommandHandler("uptime",cmd.uptime))
    dispatcher.add_handler(CommandHandler("diskusage",cmd.diskusage))
    dispatcher.add_handler(CommandHandler("temps",cmd.temps))
    dispatcher.add_handler(CommandHandler("getfilechanges",cmd.getfilechanges))

    fmonitor_thread = Thread(target=fmonitor.FileWatcher("/home/alex/test").run)
    fmonitor_thread.start()


    #start listening for chat input
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
