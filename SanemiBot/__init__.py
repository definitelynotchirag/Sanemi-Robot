from telethon.sync import TelegramClient
from telethon import events
import os
from dotenv import load_dotenv,dotenv_values;
import requests
import psycopg2;
from psycopg2 import sql
import time,datetime
import pymongo
import importlib,sys

load_dotenv()

modules_path = os.path.join(os.path.dirname(__file__), 'modules')
if modules_path not in sys.path:
    sys.path.append(modules_path)
    
    
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

mongoclient = pymongo.MongoClient(os.getenv('MONGODB'))
mydb = mongoclient["testing"]
mycol = mydb["users"]

conn = psycopg2.connect(
    host=os.getenv("DBHOST"),
    database=os.getenv("DBNAME"),
    user=os.getenv("DBUSER"),
    password=os.getenv("DBPASSWORD"),
    )

cur = conn.cursor()       
        
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
