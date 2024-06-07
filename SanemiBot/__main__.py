import importlib
import os
from SanemiBot import bot
from telethon import events

def import_all_modules(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.py'):
            module_name = file_name[:-3]
            importlib.import_module(module_name)
            
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi!I am Sanemi A Game Bot Based on Anime Demon Slayer!')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
    await event.respond('What Help Do You Need?');
    



            
if __name__ == "__main__":
    import_all_modules('SanemiBot/modules')
    bot.run_until_disconnected();