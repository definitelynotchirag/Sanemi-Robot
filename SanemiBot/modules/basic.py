from telethon import bot,events
from SanemiBot import log_channel
from SanemiBot.utils import user

@bot.on(events.NewMessage(pattern="/wallet"))
async def wallet(event):
    try:
        user_id = event.from_id.user_id
    except Exception as e:
        user_id = event.peer_id.user_id
        
    await user.checkadduser(user_id)
    try:
        wallet = await user.getwallet(user_id=user_id)
    except Exception as e:
        msg = f'''
        NEW ERROR HAS OCCURED:\n
        {str(e)}
        '''
        await bot.send_message(log_channel,msg)
        
    await event.respond(f'Wallet: `{wallet}ֆ`');

    