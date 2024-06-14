from SanemiBot import bot, LOGGER, log_channel
from SanemiBot.utils import users, groups, converter, timediff
from telethon import events

@bot.on(events.NewMessage(pattern="/top"))
async def top(event):
    user_id = event.sender_id
    if not await users.checkverified(user_id):
        return
    str1 = "# 🏆 Top Users 🏆\n\n"
    msg = await event.respond(file = "./Assets/leaderboard.jpg")
    topusers = await users.get_top_users()
    count = 0
    for user in topusers:
        user_id = user[0]  
        username = user[3]
        wallet = user[1]
        count += 1
        str1 += f"{count}. **{username}** - `{wallet}ֆ`\n"
        

    await msg.edit(str1)
