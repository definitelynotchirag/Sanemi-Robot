from SanemiBot import bot, LOGGER, log_channel
from SanemiBot.utils import users, groups, converter, timediff
from telethon import events

@bot.on(events.NewMessage(pattern="/setwallet"))
async def setwallet(event):
    if(event.message.is_reply):
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id
        wallet = event.message.text.split(' ')[1]
    else:
        user_id = event.message.text.split(' ')[1]
        wallet = event.message.text.split(' ')[2]
        
    try:
        await users.setwallet(user_id, wallet)
        await event.respond('Wallet Set!')
    except Exception as e:
        LOGGER.error(e)
        await event.respond('Invalid Argument!')