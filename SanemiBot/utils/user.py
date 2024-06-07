from SanemiBot import pool;
import psycopg2;

async def checkadduser(user_id):
    try:
        async with pool.acquire() as cur:
            await cur.execute(f"""
        INSERT INTO user_list (user_id, wallet) 
        VALUES ({user_id}, 100) 
        ON CONFLICT (user_id,wallet) DO NOTHING;
    """)
    except (psycopg2.DatabaseError, Exception) as error:
        raise error

async def getwallet(user_id):
    await checkadduser(user_id=user_id)
    try:
        async with pool.acquire() as cur:
            wallet_value = await cur.fetchval("""
                    SELECT wallet FROM user_list WHERE user_id = $1
                """, user_id)
            return wallet_value
    except (psycopg2.DatabaseError, Exception) as error:
        raise error