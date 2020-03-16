#telegram_server_stats.py
####################################################################
#entry point of the bot
#
#reads in API_TOKEN and sets up bot. Also adds all used command_blocks
####################################################################

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import command_blocks as cmd

#setup logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#read API-token
file = open('api_token.txt')
API_TOKEN = file.readline().rstrip('\n');
file.close()

#start bot and poll for user input
def main():
    updater = Updater(API_TOKEN,use_context=True)

    dispatcher = updater.dispatcher

    #add commandHandlers here:
    dispatcher.add_handler(CommandHandler("uptime",cmd.uptime))
    dispatcher.add_handler(CommandHandler("diskusage",cmd.diskusage))
    dispatcher.add_handler(CommandHandler("temps",cmd.temps))
    dispatcher.add_handler(CommandHandler("diskhealth",cmd.diskhealth))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
