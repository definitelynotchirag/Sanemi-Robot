import importlib
import os
from SanemiBot import bot,log_channel,init_db
from telethon import events, Button
import asyncio
from SanemiBot.utils import groups, users, prof, verify
import sys

pending_names = {}

def import_all_modules(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.py'):
            module_name = file_name[:-3]
            importlib.import_module(module_name)
            print(f"Imported {module_name}")
            
@bot.on(events.NewMessage)
async def adduser(event):
    sender = await event.get_sender()
    username = sender.username
    user_id = sender.id
    chat = event.chat
    chat_id = chat.id
    chat_title = chat.title if hasattr(chat, 'title') else False
    if chat_title:
         await groups.checkaddgroup(chat_id,chat_title)
    msg = event.message
    iscommand = False
    if(msg.text.startswith('/')):
        iscommand = True
        
    iswaiting = pending_names[user_id] if user_id in pending_names else False
    
        
    try:
        userrr = await users.get_user_info(user_id)
        if not userrr and chat_title is False:
            await event.reply("Hey, I am Sanemi A Game Bot Based on Anime Demon Slayer!\nLets start our journey!!",file='./Assets/introvideo.mp4',buttons = [[Button.inline("Start",data="intro")]])
            await users.checkadduser(username=username,user_id=user_id)
            
        elif not userrr and chat_title and iscommand:
            await event.reply("Hey! Meet me in Dm and Type /start to get started!",buttons = [[Button.url("Open Bot",url=f"t.me/SanemixBot")]])
        
        elif userrr and chat_title is False and userrr['nickname'] == None and not iswaiting:
            await event.reply("Welcome Back! I am Sanemi A Game Bot Based on Anime Demon Slayer!\nLets start our journey!!",file='./Assets/introvideo.mp4',buttons = [[Button.inline("Start",data="intro")]])
            await users.checkadduser(username=username,user_id=user_id)
        
        elif userrr and chat_title and userrr['nickname'] == None and iscommand:
            await event.reply("Hey You Haven't Verified Yourself Yet! Please Verify Yourself by typing /start in Dm!",buttons = [[Button.url("Open Bot",url=f"t.me/SanemixBot")]])
        else:
            await users.checkadduser(username=username,user_id=user_id)

            
            
    except Exception as e:
        msg = f'''
        NEW ERROR HAS OCCURED:\n
        {str(e)}
        '''
        
        await bot.send_message(log_channel,msg)
        
@bot.on(events.CallbackQuery(data="intro"))
async def intro(event):
    user_id = event.sender_id
    await event.edit("Kakushi will be guiding you throughout your journey.",file='./Assets/intro.jpg',
    buttons=[[Button.inline("Continue",data="intro1")]])

@bot.on(events.CallbackQuery(data="intro1"))
async def continuee(event):
    user_id = event.sender_id
    isverified = await users.checkverified(user_id)
    if(isverified):
        await event.answer("You Are Already Verified!")
        return
    await event.edit("What should we call you?\nType your name:",file='./Assets/intro2.jpg',
    buttons=[[Button.inline("Skip",data="skip")]])
    pending_names[user_id] = True
            
            
@bot.on(events.NewMessage)
async def handle_name(event):
    user_id = event.sender_id
    if user_id in pending_names and pending_names[user_id]:
        name = event.message.message
        await event.reply("Great We Are Done! You can change your name anytime by using /setnick command")
        await users.updatenickname(user_id,name)
        pending_names[user_id] = False
        return
        
        
@bot.on(events.CallbackQuery(data="skip"))
async def skip(event):
    user_id = event.sender_id
    isverified = await users.checkverified(user_id)
    if(isverified):
        await event.answer("You Are Already Verified!")
        return
    user = await bot.get_entity(user_id)
    await event.edit("Alright! You can change your name anytime by using /setnick command for now we will call you by Your username!",buttons=[[Button.inline("Continue",data="intro2")]])
    pending_names[user_id] = False
    await users.updatenickname(user.id,user.username)

    
        
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    user_id = event.sender_id
    if not await users.checkverified(user_id):
        return
    await event.reply("Hey, I am Sanemi A Game Bot Based on Anime Demon Slayer!\nLets start our journey!!",file='https://telegra.ph/file/5ec6c9fd75b534ece0152.mp4')

    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
    user_id = event.sender_id
    if not await users.checkverified(user_id):
        return
    await event.respond('What Help Do You Need?');
    
    
async def main():
    await init_db()
    await bot.run_until_disconnected()
                 
if __name__ == "__main__":
    import_all_modules('SanemiBot/modules')
    import_all_modules('SanemiBot/utils')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())