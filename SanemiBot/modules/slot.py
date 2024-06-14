from SanemiBot import bot, log_channel,LOGGER
from SanemiBot.utils import users, groups, converter, timediff
from telethon import events,types
import asyncio

@bot.on(events.NewMessage(pattern="/slot"))
async def slot(event):
    user = await event.get_sender()
    user_id = user.id
    chat_id = event.chat_id
    msg = event.message

    if not await users.checkverified(user_id):
        return
    
    if len(msg.text.split(' ')) < 2:
        await event.respond("Invalid Syntax! Use /slot <amount>")
        return
    
    ispassive = await users.checkpassive(user_id)
    if(ispassive):
        await event.respond("Your Are in Passive Mode Turn it Off by using /passive off")
        return
        
    if(chat_id):
        ison = await groups.checktoggle(user_id)
        if not ison:
            return
        
    lastslottime = await timediff.getslottime(user_id)
    if lastslottime is None:
        xx = 25
    else:
        xx = timediff.time_difference(lastslottime)
        
    if xx < 25:
        await event.respond(f"Wait! You can Slot again in {25-int(xx)} secs.")
        return
    
    tokens = await users.gettokens(user_id)
    if tokens < 1:
        await event.respond("You do not have enough tokens!")
        return
    
    # two values similar list
    tvsl = [2,3,4,5,6,9,11,13,16,17,18,21,23,24,26,27,30,32,33,35,38,39,41,42,44,47,48,49,52,54,56,59,60,61,62,63]
    # one value similar list
    ovsl = [1,22,43,64]
    
    
    amount1 = msg.text.split(' ')[1]
    amount = abs(int(converter.cstn(amount1)))

    media = types.InputMediaDice('🎰')
    ttt = await event.respond(file=media)
    z = ttt.media.value
    
    oldm = (await users.getwallet(user.id))[0]
    if amount > oldm:
        await event.respond('You do not have enough money!')
        return 
    elif z in tvsl:
        total = int(oldm) + amount
        await users.updatewallet(user.id,total)
        await users.updatetokens(user.id,tokens-1)
        await asyncio.sleep(4)
        await event.respond(f'You won! You Get : `{amount}ֆ`\nCurrent Wallet : `{total}ֆ`')
    elif z in ovsl:
        total = int(oldm) + (amount*3)
        await users.updatewallet(user.id,total)
        await users.updatetokens(user.id,tokens-1)
        await asyncio.sleep(4)
        await event.respond(f'You won! You Get thrice the amount : `{amount*3}ֆ`\nCurrent Wallet : `{total}ֆ`')
    else:
        total = int(oldm) - amount
        await users.updatewallet(user.id,total)
        await users.updatetokens(user.id,tokens-1)
        await asyncio.sleep(4)
        await event.respond(f'You lost! You lost : `{amount}ֆ`')
        
    await timediff.setslottime(user_id)
        
        
        
    