from SanemiBot import bot, LOGGER, log_channel
from SanemiBot.utils import users, groups, converter, timediff
from time import gmtime
from time import strftime
from telethon import events
import random, asyncio
from numerize import numerize

@bot.on(events.NewMessage(pattern="/daily"))
async def daily(event):
    user = await event.get_sender()
    user_id = user.id
    chat_id = event.chat_id
    msg = event.message
    
    if not await users.checkverified(user_id):
        return
    
    ispassive = await users.checkpassive(user_id)
    if(ispassive):
        await event.respond("Your Are in Passive Mode Turn it Off by using /passive off")
        return
        
    if(chat_id):
        ison = await groups.checktoggle(user_id)
        if not ison:
            return
        
    lastdailytime = await timediff.getdailytime(user_id)
    if lastdailytime is None:
        xx = 86400
    else:
        xx = timediff.time_difference(lastdailytime)
        htime = strftime("%H:%M:%S", gmtime(86400-int(xx)))
        
    if xx < 86400:  
        await event.respond(f"Wait! You can Daily again in {htime} hrs.")
        return

    diamondprob = [1,2,3]
    tokenprob = [1,2,3]
    
    msgg = await event.reply("Choosing Probabilites...")
    await asyncio.sleep(1)
    
    userinfo = await users.get_user_info(user_id)
    wallet = userinfo['wallet']
    
    diamonds = userinfo['diamonds']
    tokens = userinfo['tokens']
    
    morediamond = random.choice(diamondprob)
    moretoken = random.choice(tokenprob)
    
    await bot.edit_message(event.chat_id, msgg.id, "Calculating Rewards...")
    await asyncio.sleep(1)
    
    amount = 25000
    numerizedamount = numerize.numerize(amount, 3)
    
    await users.updatediamonds(user_id, diamonds + morediamond)
    await users.updatetokens(user_id, tokens + moretoken)
    await users.updatewallet(user_id, wallet + amount)
    
    await bot.edit_message(event.chat_id, msgg.id, f"Daily Rewards:\n\n💰 `{numerizedamount}ֆ`\n💎 `{morediamond}` Diamonds\n🎟️ `{moretoken}` Tokens")

    await timediff.setdailytime(user_id)
    
    
    
    
    


    