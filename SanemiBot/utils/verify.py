from SanemiBot import get_db,log_channel,bot,LOGGER
from SanemiBot.utils import groups,converter,users,timediff

async def updateverified(user_id):
    db = await get_db()
    await db.execute("UPDATE user_list SET isverified = 1 WHERE user_id = ?",(user_id,))
    await db.commit()
    LOGGER.info(f"User {user_id} has been verified")