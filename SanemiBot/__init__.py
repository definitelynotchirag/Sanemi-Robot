from telethon.sync import TelegramClient
from telethon import events
from supabase import create_client, Client
import os
from dotenv import load_dotenv,dotenv_values;
import requests,asyncio
import asyncpg
import psycopg2;
from psycopg2 import sql
import time,datetime
import pymongo
import importlib,sys
import logging

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger("telethon").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

modules_path = os.path.join(os.path.dirname(__file__), 'modules')
if modules_path not in sys.path:
    sys.path.append(modules_path)
    
utils_path = os.path.join(os.path.dirname(__file__), 'utils')
if utils_path not in sys.path:
    sys.path.append(utils_path)
    
    
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
log_channel = os.getenv("LOG_CHANNEL")

mongoclient = pymongo.MongoClient(os.getenv('MONGODB'))
mydb = mongoclient["testing"]
mycol = mydb["users"]

pool = None

async def init_pool():
    global pool
    pool = await asyncpg.create_pool(
        host=os.getenv("DBHOST"),
        database=os.getenv("DBNAME"),
        user=os.getenv("DBUSER"),
        password=os.getenv("DBPASSWORD"))


conn = psycopg2.connect(
    host=os.getenv("DBHOST"),
    database=os.getenv("DBNAME"),
    user=os.getenv("DBUSER"),
    password=os.getenv("DBPASSWORD"),
    )

cur = conn.cursor()       
        
        
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

loop = asyncio.get_event_loop()
loop.run_until_complete(init_pool())