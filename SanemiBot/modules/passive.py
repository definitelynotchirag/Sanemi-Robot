from SanemiBot import bot,LOGGER,log_channel
from SanemiBot.utils import users, groups, converter, timediff
from telethon import events

@bot.on(events.NewMessage(pattern="/passive"))
async def passive(event):
    try:
        ps = event.message.text.split(' ')[1]
    except IndexError:
        await event.respond("Invalid argument! Use 'on' or 'off'!")
        return
    
    if ps in ['on', 'true']:
        arg = True
    elif ps in ['off', 'false']:
        arg = False
    else:
        await event.respond("Invalid argument! Use 'on' or 'off'!")
        return
    
    user_id = event.sender_id
    try:
        ispassive = await users.checkpassive(user_id)
        if ispassive and not arg:
            await users.setpassive(user_id, arg)
            await event.respond('You are no longer passive!')
        elif not ispassive and arg:
            await users.setpassive(user_id, arg)
            await event.respond('You are now passive!')
        else:
            await event.respond('You Already Are What You Are!')
    except Exception as e:
        LOGGER.error(e)