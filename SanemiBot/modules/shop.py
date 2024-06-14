from SanemiBot import bot, LOGGER, log_channel
from telethon import events, Button
from SanemiBot.utils import users, groups, converter, timediff
from telethon.types import ReplyKeyboardMarkup, KeyboardButton


@bot.on(events.NewMessage(pattern="/shop"))
async def shop(event):
    user = await event.get_sender()
    user_id = user.id
    chat_id = event.chat_id
    msg = event.message
    
    if not await users.checkverified(user_id):
        return
    
    if(chat_id):
        ison = await groups.checktoggle(user_id)
        if not ison:
            return
    
    userinfo = await users.get_user_info(user_id)
    wallet = userinfo['wallet']
    diamonds = userinfo['diamonds']
    tokens = userinfo['tokens']
    custom_keyboard = ReplyKeyboardMarkup(
        [
                [KeyboardButton(text="Deals")],
                [KeyboardButton(text="Weapons")],
                [KeyboardButton(text="Food")]
                ],
        resize=True,
        single_use=True
    )
    
    await event.reply(file="./Assets/shop.jpg", message=f"SHOP\nBuy Items Here Using Coins or Diamonds.\nYour Wallet: {wallet}ֆ\nYour Diamonds: {diamonds}\nYour Tokens: {tokens}"
    ,buttons=[
    [Button.inline('Weapons', data="sweapons"), Button.inline('Food', data="sfood")]
    
])
    
@bot.on(events.CallbackQuery(data="sweapons"))
async def handle_weapons(event):
    await event.edit("You clicked on Weapons. Here is a list of weapons...",buttons=[
        [Button.inline('Sword', data="sword"), Button.inline('Gun', data="gun")],
        [Button.inline('Back', data="back")]
    ])

@bot.on(events.CallbackQuery(data="sfood"))
async def handle_food(event):
    await event.edit("You clicked on Food. Here is a list of food items...",
    buttons=[
        [Button.inline('Sakura Mochi', data='sakura')], [Button.inline('Ramen', data='ramen')],
        [Button.inline('Odon', data='odon')],
        [Button.inline('Back', data="back")]
    ])
    
@bot.on(events.CallbackQuery(data="sakura"))
async def handle_sakura(event):
    await event.edit("Sakura Mochi",file="./Assets/sakuramochi.jpg",buttons=[
       [Button.inline('Back', data="back")]
    ])
    
@bot.on(events.CallbackQuery(data="ramen"))
async def handle_ramen(event):
    await event.edit("Ramen",file="./Assets/ramen.jpg",buttons=[
       [Button.inline('Back', data="back")]
    ])
    
@bot.on(events.CallbackQuery(data="odon"))
async def handle_odon(event):
    await event.edit("Odon",file="./Assets/odon.jpg",buttons=[
       [Button.inline('Back', data="back")]
    ])
    
@bot.on(events.CallbackQuery(data="back"))
async def handle_back(event):
    # msg = await event.get_message()
    # if event.from_user.id != msg.get_reply_message().from_id:
    #     await event.answer("Open Your Own SHOP by /shop",show_alert = True)
    #     return

    await event.edit("SHOP\nBuy Items Here Using Coins or Diamonds.",file="https://telegra.ph/file/f54efe6d8bd0d0108885d.jpg"
    ,buttons=[
    [Button.inline('Weapons', data="sweapons"), Button.inline('Food', data="sfood")]
    
])
    
@bot.on(events.CallbackQuery(data="sword"))
async def handle_sword(event):
    await event.edit("Here is The List of Swords: ",buttons=[
         [Button.inline('Back', data="back")]
    ])
    
