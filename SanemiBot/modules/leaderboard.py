from SanemiBot import bot, LOGGER, log_channel
from SanemiBot.utils import users, groups, converter, timediff
from telethon import events

@bot.on(events.NewMessage(pattern="/top"))
async def top(event):
    str1 = "🏆𝗟𝗘𝗔𝗗𝗘𝗥𝗕𝗢𝗔𝗥𝗗 ⫶\n\n"
    msg = await event.respond(file = "https://telegra.ph/file/a23ad4b0691af4d44cc31.jpg")
    topusers = await users.get_top_users()
    count = 0
    for user in topusers:
        user_id = user[0]  
        username = user[3]
        wallet = user[1]
        count += 1
        str1 += f"{count}. **{username}** - `{wallet}ֆ`\n"
        

    await msg.edit(str1)
