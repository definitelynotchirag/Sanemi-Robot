import psycopg2;
from psycopg2 import sql
import time,datetime
import pymongo
from telethon import events
from SanemiBot import bot,cur,mycol,conn,supabase,pool

@bot.on(events.NewMessage(pattern='/sql'))
async def allusers(event):
    user_id = event.from_id.user_id

    timestamp = datetime.datetime(2024, 5, 27, 19, 59, 2, 450434, tzinfo=datetime.timezone.utc)
    score = 200

    # Insert query using parameterized statement
    try:
        query = sql.SQL('INSERT INTO user_list (user_id, created_at, wallet) VALUES (%s, %s, %s)')
        rl = cur.execute(query, (user_id, timestamp, score))
        conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        # cur.execute("ROLLBACK")
        # conn.commit()
        await event.respond(str(error))
        
    cur.execute(f'SELECT user_id, wallet FROM user_list WHERE user_id={user_id}')
    row = cur.fetchone()
    conn.commit()
    await event.respond(f"I have inserted you to SQL Database. You Are:\n {str(row)}")
    
    
@bot.on(events.NewMessage(pattern='/mongo'))
async def api(event):
    user_id = event.from_id
    result = mycol.insert_one({'user_id':f'{user_id}'});
    if(result):
        await event.respond(f"I have inserted you to mongo Database. You Are:\n{mycol.find_one({'user_id':f'{user_id}'})}")
        
@bot.on(events.NewMessage(pattern='/sb'))
async def supabasef(event):
    user_id = event.from_id.user_id
    data, count = supabase.table('user_list').insert({"user_id": user_id, "wallet": 2000}).execute()
    if(data):
        response = supabase.table('user_list').select('user_id, wallet').eq('user_id', user_id).execute()
        print(response)
        await event.respond(str(response.data))
        
        
@bot.on(events.NewMessage(pattern='/as'))
async def aspg(event):
    try:
        user_id = event.from_id.user_id
    except Exception as e:
        user_id = event.peer_id.user_id
        
    timestamp = datetime.datetime(2024, 5, 27, 19, 59, 2, 450434, tzinfo=datetime.timezone.utc)
    score = 200

    # Insert query using parameterized statement
    # try: 
    # async with pool.acquire() as connection:
    #         # query = sql.SQL('INSERT INTO user_list (user_id, created_at, wallet) VALUES (%s, %s, %s)')
    #         rl = await connection.execute(f'INSERT INTO user_list (user_id, created_at, wallet) VALUES ({user_id},{timestamp},{score})')
    async with pool.acquire() as connection:
        await connection.execute("""
            INSERT INTO user_list (user_id, created_at, wallet)
            VALUES ($1, $2, $3)
            ON CONFLICT (user_id,wallet) DO NOTHING
        """, user_id, timestamp, score)
    # except (psycopg2.DatabaseError, Exception) as error:
    #     # cur.execute("ROLLBACK")
    #     # conn.commit()
    #     print(Exception)
    #     await event.respond(str(error))
    
    async with pool.acquire() as connection:
        row = await connection.fetchrow(f'SELECT user_id, wallet FROM user_list WHERE user_id={user_id}')
        
    await event.respond(f"I have inserted you to SQL Database. You Are:\n {str(row)}")
    