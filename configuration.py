import csv

def read_config():
    with open("config.csv") as file:
        config=dict(filter(None, csv.reader(file)))
    return config

def get_API_TOKEN():
    config=read_config()
    return config["API_TOKEN"]

def get_CHAT_ID():
    config=read_config()
    return config["CHAT_ID"]
