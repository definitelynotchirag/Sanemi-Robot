import datetime
from SanemiBot import get_db
def time_difference(previous_time):
    previous_timee = datetime.datetime.fromisoformat(previous_time).replace(tzinfo=datetime.timezone.utc)
    current_time = datetime.datetime.now(datetime.timezone.utc)
    difference = current_time - previous_timee
    return difference.total_seconds()



async def getbettime(user_id):
    """
    Get the time of the last bet made by the user.
    
    Parameters:
    user_id (int): The user ID.
    
    Returns:
    str: The time of the last bet made by the user.
    """
    
    db = await get_db()
    try:
        async with db.execute("SELECT betted_at FROM timedata WHERE user_id = ?", (user_id,)) as cursor:
            betted_at = await cursor.fetchone()
            return betted_at[0] if betted_at else None
        
    except Exception as e:
        raise e

async def setbettime(user_id):
    """
    Set the time of the last bet made by the user to the current time.
    
    Parameters:
    user_id (int): The user ID.
    """
    
    db = await get_db()
    try:
            await db.execute("""
                UPDATE timedata SET betted_at = CURRENT_TIMESTAMP WHERE user_id = ?;
            """, (user_id,))  
            await db.commit()
    except Exception as e:
        raise e
    
    
async def getslottime(user_id):
    """
    Get the time of the last slot made by the user.
    
    Parameters:
    user_id (int): The user ID.
    
    Returns:
    str: The time of the last slot made by the user.
    """
    
    db = await get_db()
    try:
        async with db.execute("SELECT slot_at FROM timedata WHERE user_id = ?", (user_id,)) as cursor:
            slot_at = await cursor.fetchone()
            return slot_at[0] if slot_at else None
        
    except Exception as e:
        raise e
    
async def setslottime(user_id):
    """
    Set the time of the last slot made by the user to the current time.
    
    Parameters:
    user_id (int): The user ID.
    """
    
    db = await get_db()
    try:
            await db.execute("""
                UPDATE timedata SET slot_at = CURRENT_TIMESTAMP WHERE user_id = ?;
            """, (user_id,))  
            await db.commit()
    except Exception as e:
        raise e
    
    
async def getdailytime(user_id):
    """
    Get the time of the last daily claimed by the user.
    
    Parameters:
    user_id (int): The user ID.
    
    Returns:
    str: The time of the last daily claimed by the user.
    """
    
    db = await get_db()
    try:
        async with db.execute("SELECT daily_at FROM timedata WHERE user_id = ?", (user_id,)) as cursor:
            daily_at = await cursor.fetchone()
            return daily_at[0] if daily_at else None
        
    except Exception as e:
        raise e
    
async def setdailytime(user_id):
    """
    Set the time of the last daily claimed by the user to the current time.
    
    Parameters:
    user_id (int): The user ID.
    """
    
    db = await get_db()
    try:
            await db.execute("""
                UPDATE timedata SET daily_at = CURRENT_TIMESTAMP WHERE user_id = ?;
            """, (user_id,))  
            await db.commit()
    except Exception as e:
        raise e