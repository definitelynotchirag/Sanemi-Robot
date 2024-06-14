from SanemiBot import bot, logging, LOGGER
from telethon import events
from SanemiBot.utils import users,prof


@bot.on(events.NewMessage(pattern='/profile'))
async def profile(event):
    user_id = event.sender_id
    if not await users.checkverified(user_id):
        return
    user = await bot.get_entity(user_id)
    user_info = await users.get_user_info(user_id)
    if not user:
        return
    text = f"**First Name:** {user.first_name}\n**Last Name:** {user.last_name}\n**Username:** {user.username}\n**User ID:** {user.id}\n**Wallet:** {user_info['wallet']}\n**Passive**: {user_info['ispassive']}\n**Diamonds:** {user_info['diamonds']}"
    userhp = user_info['hp']
    text += f"\n\n**Health:** {user_info['hp']}\n[{prof.make_bar(int(prof.get_percentage(200,userhp)))}{prof.get_percentage(200,userhp)}%]"
    
    await event.reply(text)
    LOGGER.info(f"Profile of {user_id} sent")
    

