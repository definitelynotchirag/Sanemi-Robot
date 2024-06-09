from SanemiBot import bot, get_db,LOGGER

async def checkaddgroup(groupid,groupname):
    db = await get_db()
    try:
        async with db.execute("""
            INSERT INTO grouplist (groupid, groupname)
            VALUES (?, ?)
            ON CONFLICT (groupid) DO NOTHING;
        """, (groupid, groupname)) as cursor:
            await db.commit()
    except Exception as e:
        raise e
        LOGGER.error(str(e))
        
async def checktoggle(groupid):
    db = await get_db()
    try:
        async with db.execute("""
            SELECT toggle FROM grouplist
            WHERE groupid = ?;
        """, (groupid,)) as cursor:
            ison = await cursor.fetchone()
        if ison:
            return bool(ison[0])
        else:
            return True
    except Exception as e:
        raise e
        LOGGER.error(str(e))
    
    
    