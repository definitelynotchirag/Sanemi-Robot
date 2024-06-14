from telethon import events
from numerize import numerize
import random,asyncio,datetime
from SanemiBot import get_db,log_channel,bot,LOGGER
from SanemiBot.utils import groups,converter,users,timediff
from datetime import timezone

print("Imported bet.py HAHAHAHAHAAH")
@bot.on(events.NewMessage(pattern="/bet"))
async def bet(event):
    try:
        user_id = event.from_id.user_id
        chat = event.chat
        chat_id = chat.id
    except Exception as e:
        user_id = event.peer_id.user_id
        chat_id = None
    
    ispassive = await users.checkpassive(user_id)
    if(ispassive):
        await event.respond("Your Are in Passive Mode Turn it Off by using /passive off")
        return
        
    if(chat_id):
        ison = await groups.checktoggle(user_id)
        if not ison:
            return
        
    try:
        msg = event.message
        
        if len(msg.text.split(' ')) < 3:
            await event.respond("Invalid Syntax! Use /bet <amount> <black/white>")
            return
        
        lastbettime = await timediff.getbettime(user_id)
        if lastbettime is None:
            xx = 20
        else:
            xx = timediff.time_difference(lastbettime)

        if xx < 20:
            await event.respond(f"Wait! You can bet again in {20-int(xx)} secs.")
            return

        userchoice = msg.text.split(' ')[-1]
        amount1 = msg.text.split(' ')[1]
        amount = abs(int(converter.cstn(amount1)))
        numerizedbetamount = numerize.numerize(amount, 3)
        

        if userchoice in ['b', 'black']:
            usrchoice = "black"
        elif userchoice in ['w', 'white']:
            usrchoice = "white"
        else:
            await event.respond("Invalid Choice! Choose between Black or White")
            return

        choice = random.choice(['black', 'white'])

        message = await event.respond( '⚫')
        await asyncio.sleep(0.2)
        
        await bot.edit_message(event.chat_id, message.id, '⚪')
        await asyncio.sleep(0.2)
        
        if(choice == 'black'):
            try:
                await bot.edit_message(event.chat_id, message.id, '⚫')
            except Exception as e:
                pass
        else:
            try:
                await bot.edit_message(event.chat_id, message.id, '⚪')
            except Exception as e:
                pass

        if usrchoice.lower() == choice:
            oldm = abs(int((await users.getwallet(user_id))[0]))
            if amount > oldm:
                await event.respond("Bet Something which you can afford")
            else:
                newm =  oldm + amount
                await users.updatewallet(user_id, newm)
                await bot.edit_message(event.chat_id, message.id, f"You Won! Added {numerizedbetamount} to your wallet.")
        else:
            oldm = abs(int((await users.getwallet(user_id))[0]))
            if amount > oldm:
                await bot.edit_message(event.chat_id, message.id,"You don't have enough Money to bet.")
            else:
                newm =  oldm - amount
                await users.updatewallet(user_id, newm)
                await bot.edit_message(event.chat_id, message.id,f"Lost!Took {numerizedbetamount} from your wallet.")
                
        await timediff.setbettime(user_id)
                
    except Exception as e:
        raise e
        LOGGER.error(e)
        
        
                
    
    
    
    