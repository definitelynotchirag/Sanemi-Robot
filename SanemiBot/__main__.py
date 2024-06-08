import importlib
import os
from SanemiBot import bot,log_channel,init_db
from telethon import events
import asyncio
from SanemiBot.utils import user

def import_all_modules(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.py'):
            module_name = file_name[:-3]
            importlib.import_module(module_name)
            
@bot.on(events.NewMessage)
async def adduser(event):
    try:
        user_id = event.from_id.user_id
    except Exception as e:
        user_id = event.peer_id.user_id
        
    try:
        await user.checkadduser(user_id=user_id)
    except Exception as e:
        msg = f'''
        NEW ERROR HAS OCCURED:\n
        {str(e)}
        '''
        
        await bot.send_message(log_channel,msg)
        
        
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi!I am Sanemi A Game Bot Based on Anime Demon Slayer!')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
    await event.respond('What Help Do You Need?');


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

    
async def main():
    await init_db()
    await bot.run_until_disconnected()
                 
if __name__ == "__main__":
    import_all_modules('SanemiBot/modules')
    import_all_modules('SanemiBot/utils')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())