from telethon import events
from SanemiBot import log_channel,bot
from SanemiBot.utils import users


@bot.on(events.NewMessage(pattern="/wallet"))
async def wallet(event):
    
    # if(event.message.is_reply):
    #     reply_message_id = event.message.reply_to.reply_to_msg_id
    #     reply_message = await event.client.get_messages(event.message.chat_id, ids=reply_message_id)
    #     user_id = reply_message.sender_id
    if(event.message.is_reply):
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id  
    else:
        try:
            user_id = event.from_id.user_id
        except Exception as e:
            user_id = event.peer_id.user_id
            
    sender = await bot.get_entity(user_id)
    first_name = sender.first_name if sender.first_name else sender.username
    
    await users.checkadduser(user_id)
    try:
        wallet = await users.getwallet(user_id=user_id)
    except Exception as e:
        msg = f'''
        NEW ERROR HAS OCCURED:\n
        {str(e)}
        '''
        await bot.send_message(log_channel,msg)
        
    await event.respond(f"{first_name}'s Wallet: `{wallet}ֆ`");

    