from SanemiBot import get_db,LOGGER;


async def checkadduser(user_id,username = "SanemiUser"):
    db = await get_db()
    try:
        
                await db.execute("BEGIN")
                await db.execute("""
                    INSERT INTO user_list (user_id, wallet) 
                    VALUES (?, 100)
                    ON CONFLICT (user_id) DO NOTHING;
                """, (user_id,))
                await db.execute("""
                    INSERT INTO timedata (user_id, created_at)
                    VALUES (?, CURRENT_TIMESTAMP)
                    ON CONFLICT (user_id) DO NOTHING;
                """, (user_id,))
                await db.commit()
            # await db.execute("""
            #     INSERT INTO user_list (user_id, wallet) 
            #     VALUES (?, 100)
            #     ON CONFLICT (user_id) DO NOTHING;
            #     INSERT INTO timedata (user_id, created_at)
            #     VALUES (?, CURRENT_TIMESTAMP)
            #     ON CONFLICT (user_id) DO NOTHING;
            # """, (user_id,))
            # # await db.execute("""
            #     INSERT INTO timedata (user_id, created_at)
            #     VALUES (?, CURRENT_TIMESTAMP);
            #     ON CONFLICT (user_id) DO NOTHING
            # """, (user_id,))
            # await db.commit()
    except  Exception as error:
        raise error
    

async def get_user_info(user_id):
    db = await get_db()
    async with db.execute("SELECT * FROM user_list WHERE user_id = ?", (user_id,)) as cursor:
        row = await cursor.fetchone()
        if row:
            columns = [column[0] for column in cursor.description]
            user_dict = dict(zip(columns, row))
            return user_dict
        else:
            return None

async def getwallet(user_id):
    db = await get_db()
    await checkadduser(user_id=user_id)
    try:

        cursor = await db.execute(f"""
                            SELECT wallet,diamonds FROM user_list WHERE user_id = {user_id};
                        """)
        wallet_value = await cursor.fetchone()
        return wallet_value
    except Exception as error:
        raise error
    
async def updatewallet(user_id,amount):
    db = await get_db()
    try:
        cursor = await db.execute(f"""
                                  UPDATE user_list SET wallet = {amount} WHERE user_id = {user_id};
                                  """)
        await db.commit()
    except Exception as error:
        LOGGER.error(error)
    
    
async def setwallet(user_id,amount):
    db = await get_db()
    try:
        cursor = await db.execute(f"""
                                  UPDATE user_list SET wallet = {amount} WHERE user_id = {user_id};
                                  """)
        await db.commit()
    except Exception as error:
        LOGGER.error(error)
    
    
async def gettokens(user_id):
    db = await get_db()
    await checkadduser(user_id=user_id)
    try:

        cursor = await db.execute(f"""
                            SELECT tokens FROM user_list WHERE user_id = {user_id};
                        """)
        wallet_value = await cursor.fetchone()
        return wallet_value[0]
    except Exception as error:
        raise error
    
async def updatetokens(user_id,amount):
    db = await get_db()
    try:
        cursor = await db.execute(f"""
                                  UPDATE user_list SET tokens = {amount} WHERE user_id = {user_id};
                                  """)
        await db.commit()
    except Exception as error:
        LOGGER.error(error)
    
    
async def getdiamonds(user_id):
    db = await get_db()
    await checkadduser(user_id=user_id)
    try:

        cursor = await db.execute(f"""
                            SELECT diamonds FROM user_list WHERE user_id = {user_id};
                        """)
        wallet_value = await cursor.fetchone()
        return wallet_value[0]
    except Exception as error:
        raise error
    
async def updatediamonds(user_id,amount):
    db = await get_db()
    try:
        cursor = await db.execute(f"""
                                  UPDATE user_list SET diamonds = {amount} WHERE user_id = {user_id};
                                  """)
        await db.commit()
    except Exception as error:
        LOGGER.error(error)
        
        
async def checkpassive(user_id):
    db = await get_db()
    try:
        cursor = await db.execute(f"""
                                  SELECT ispassive FROM user_list WHERE user_id = {user_id};          
                                  """)
        ispassive = await cursor.fetchone()
        return bool(ispassive[0])
    except Exception as error:
        LOGGER.error(error)
        
        
async def setpassive(user_id, ispassive):
    db = await get_db()
    try:
        cursor = await db.execute(f"""
                                  UPDATE user_list SET ispassive = {ispassive} WHERE user_id = {user_id};
                                  """)
    except Exception as error:
        LOGGER.error(error)
    

async def get_top_users():
    db = await get_db()
    try:
        async with db.execute("SELECT * FROM user_list ORDER BY wallet DESC LIMIT 10") as cursor:
            rows = await cursor.fetchall()
            return rows
    
    except Exception as error:
        raise error
    
async def get_all_users():
    db = await get_db()
    try:
        async with db.execute("SELECT * FROM user_list") as cursor:
            rows = await cursor.fetchall()
            return rows
    except Exception as error:
        raise error
        
        
async def editusernames(user_id,username):
    db = await get_db()
    try:
        cursor = await db.execute("""
            UPDATE user_list SET username = ? WHERE user_id = ?;
            """, (username, user_id))
        await db.commit()
    except Exception as error:
        LOGGER.error(error)