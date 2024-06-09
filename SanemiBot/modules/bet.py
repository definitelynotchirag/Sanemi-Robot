from telethon import events
from numerize import numerize
import random,asyncio
from SanemiBot import get_db,log_channel,bot
from SanemiBot.utils import groups,converter,users

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
        ison= await groups.checktoggle(user_id)
        if not ison:
            return
        
    try:
        msg = event.message

        userchoice = msg.text.split(' ')[-1]
        amount1 = msg.text.split(' ')[1]
        amount = abs(int(converter.cstn(amount1)))
        numerizedbetamount = numerize.numerize(amount, 3)
        
        message = await event.respond( '⚫')
        await asyncio.sleep(0.2)

        if userchoice == "b":
            usrchoice = "black"
        elif userchoice == "w":
            usrchoice = "white"
        else:
            usrchoice = userchoice

        choice = random.choice(['black', 'white'])

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
            oldm = abs(int(await users.getwallet(user_id)))
            if amount > oldm:
                await event.respond("Bet Something which you can afford")
            else:
                newm =  oldm + amount
                await users.updatewallet(user_id, newm)
                await bot.edit_message(event.chat_id, message.id, f"You Won! Added {numerizedbetamount} to your wallet.")
        else:
            oldm = abs(int(await users.getwallet(user_id)))
            if amount > oldm:
                await bot.edit_message(event.chat_id, message.id,"You don't have enough Money to bet.")
            else:
                newm =  oldm - amount
                await users.updatewallet(user_id, newm)
                await bot.edit_message(event.chat_id, message.id,f"Lost!Took {numerizedbetamount} from your wallet.")
                
    except Exception as e:
        raise e
        # print(f"An error occurred: {e}")
        
        
                
    
    
    
    