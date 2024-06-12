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
        

@bot.on(events.NewMessage(pattern="/settokens"))
async def settokens(event):
    if(event.message.is_reply):
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id
        tokens = event.message.text.split(' ')[1]
    else:
        user_id = event.message.text.split(' ')[1]
        tokens = event.message.text.split(' ')[2]
        
    try:
        await users.updatetokens(user_id, tokens)
        await event.respond('Tokens Set!')
    except Exception as e:
        LOGGER.error(e)
        await event.respond('Invalid Argument!')
        
    
@bot.on(events.NewMessage(pattern="/setdiamonds"))
async def setdiamonds(event):
    if(event.message.is_reply):
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id
        diamonds = event.message.text.split(' ')[1]
    else:
        user_id = event.message.text.split(' ')[1]
        diamonds = event.message.text.split(' ')[2]
        
    try:
        await users.updatediamonds(user_id, diamonds)
        await event.respond('Diamonds Set!')
    except Exception as e:
        LOGGER.error(e)
        await event.respond('Invalid Argument!')