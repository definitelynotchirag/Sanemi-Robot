from SanemiBot import get_db;


async def checkadduser(user_id):
    db = await get_db()
    try:
        await db.execute(f"""
                        INSERT INTO user_list (USERID, WALLET) 
                        VALUES ({user_id}, 100) 
                        ON CONFLICT (USERID) DO NOTHING;
                    """)
        await db.commit()
    except  Exception as error:
        raise error

async def getwallet(user_id):
    db = await get_db()
    await checkadduser(user_id=user_id)
    try:

        cursor = await db.execute(f"""
                            SELECT wallet FROM user_list WHERE USERID = {user_id}
                        """)
        wallet_value = await cursor.fetchone()
        return wallet_value[0]
    except Exception as error:
        raise error
    