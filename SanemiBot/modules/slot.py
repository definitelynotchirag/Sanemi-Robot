from SanemiBot import bot, log_channel,LOGGER
from SanemiBot.utils import users, groups, converter, timediff
from telethon import events,types
import asyncio

@bot.on(events.NewMessage(pattern="/slot"))
async def slot(event):
    
    # two values similar list
    tvsl = [2,3,4,5,6,9,11,13,16,17,18,21,23,24,26,27,30,32,33,35,38,39,41,42,44,47,48,49,52,54,56,59,60,61,62,63]
    # one value similar list
    ovsl = [1,22,43,64]
    
    
    user = await event.get_sender()
    chatid = event.chat_id
    msg = event.message
    
    if len(msg.text.split(' ')) < 2:
        await event.respond("Invalid Syntax! Use /slot <amount>")
        return
    
    amount = int(msg.text.split(' ')[1])

    media = types.InputMediaDice('🎰')
    ttt = await event.respond(file=media)
    z = ttt.media.value
    
    oldm = await users.getwallet(user.id)
    if amount > oldm:
        await event.respond('You do not have enough money!')
        return 
    elif z in tvsl:
        total = int(oldm) + amount
        await users.updatewallet(user.id,total)
        await asyncio.sleep(4)
        await event.respond(f'You won! Your Get : `{amount}ֆ`\nCurrent Wallet : `{total}ֆ`')
    elif z in ovsl:
        total = int(oldm) + (amount*3)
        await users.updatewallet(user.id,total)
        await asyncio.sleep(4)
        await event.respond(f'You won! Your Get thrice the amount : `{amount*3}ֆ`\nCurrent Wallet : `{total}ֆ`')
    else:
        total = int(oldm) - amount
        await users.updatewallet(user.id,total)
        await asyncio.sleep(4)
        await event.respond(f'You lost! Your lost : `{amount}ֆ`')
        
        
        
    