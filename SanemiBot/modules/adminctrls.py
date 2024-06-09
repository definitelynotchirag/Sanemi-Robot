from telethon import events
from SanemiBot import bot
from SanemiBot.utils import users


@bot.on(events.NewMessage(pattern="/updateusernames"))
async def updateusernames(event):
    allusers = await users.get_all_users()
    for user in allusers:
        user_id = user[0]
        try:
            user = await bot.get_entity(user_id)
            username = user.username
            await users.editusernames(user_id,username)
        except Exception as e:
            pass