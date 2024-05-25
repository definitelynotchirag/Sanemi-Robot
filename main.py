from telethon.sync import TelegramClient
from telethon import events
import os
from dotenv import load_dotenv,dotenv_values;

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi!I am Sanemi A Game Bot Based on Anime Demon Slayer!')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
    await event.respond('What Help Do You Need?');

# @bot.on(events.NewMessage)
# async def echo(event):
#     """Echo the user message."""
#     await event.respond(event.text)

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()