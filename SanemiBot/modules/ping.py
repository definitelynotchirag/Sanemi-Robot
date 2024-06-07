from telethon.sync import TelegramClient
from telethon import events
import time
from SanemiBot import bot

@bot.on(events.NewMessage(pattern="/ping"))
async def ping(event):
    start = time.time()
    message = await event.respond('Pong!')
    end = time.time()
    response_time = int((end - start) * 1000)  
    await bot.edit_message(event.chat_id, message.id, f'Pong! 🏓\nResponse time: {response_time} ms')
    
    