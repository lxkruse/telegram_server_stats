#command_blocks.py
####################################################################
#adds all important command command_blocks that handle user requests
#
#commands currently include /uptime,/diskusage,/temps
####################################################################

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from math import trunc
from psutil._common import bytes2human
import psutil
import time
import logging

#reply with uptime of system
def uptime(update,context):
    seconds_elapsed = time.time() - psutil.boot_time()
    hours=trunc(seconds_elapsed//3600)
    minutes=trunc((seconds_elapsed//60)%60)
    update.message.reply_text("up scince: " + str(hours)+"h"+str(minutes)+"m")

#reply with diskusage
def diskusage(update,context):
    disk_usage = psutil.disk_usage('/')
    used=bytes2human(disk_usage.used)
    total=bytes2human(disk_usage.total)
    update.message.reply_text(used+" / "+total+" used")

#reply with temps of hardware devices
def temps(update,context):
    temp_string=""
    temperatures = psutil.sensors_temperatures()
    for device,values in temperatures.items():
        temp_string+=device+"\n"
        for value in values:
            temp_string+="  "+value.label + "        " +str(value.current) + "°C"
            temp_string+="\n"
    update.message.reply_text(temp_string)
