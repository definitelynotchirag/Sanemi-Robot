import psycopg2;
from psycopg2 import sql
import time,datetime
import pymongo
from telethon import events
from SanemiBot import bot,cur,mycol

@bot.on(events.NewMessage(pattern='/sql'))
async def allusers(event):
    user_id = event.from_id.user_id

    timestamp = datetime.datetime(2024, 5, 27, 19, 59, 2, 450434, tzinfo=datetime.timezone.utc)
    score = 200

    # Insert query using parameterized statement
    try:
        query = sql.SQL('INSERT INTO user_list (user_id, created_at, wallet) VALUES (%s, %s, %s)')
        rl = cur.execute(query, (user_id, timestamp, score))
    except (psycopg2.DatabaseError, Exception) as error:
        await event.respond(str(error))
        
    cur.execute(f'SELECT user_id, wallet FROM user_list WHERE user_id={user_id}')
    row = cur.fetchone()
    await event.respond(f"I have inserted you to SQL Database. You Are:\n {str(row)}")
    
    
@bot.on(events.NewMessage(pattern='/mongo'))
async def api(event):
    user_id = event.from_id
    result = mycol.insert_one({'user_id':f'{user_id}'});
    if(result):
        await event.respond(f"I have inserted you to mongo Database. You Are:\n{mycol.find_one({'user_id':f'{user_id}'})}")