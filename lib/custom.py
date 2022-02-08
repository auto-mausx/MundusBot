import random
# Add your custom commands here | If you plan on writing one, I strongly recommend checking out the telegram API docs

### Stickers ###

def samsayingyes(update, context):
    custom_sticker = 'CAACAgEAAxkBAAEDMilhftTjxn88VqCiCqYhGh0XxD8T9AACIAIAAjzdyEe2g_Klt73eNCEE'
    context.bot.send_sticker(
            chat_id=update.effective_chat.id, sticker=custom_sticker)

def jefferysayingyes(update, context):
     custom_sticker = 'CAACAgEAAxkBAAMZYfcBY2tEtYpt6u5Tcoan_p5LdOAAArEBAAJNAXFF5MB7A9HduBojBA'
     context.bot.send_sticker(
        chat_id=update.effective_chat.id, sticker=custom_sticker)

def forcefulyes(update, context):
     custom_sticker = 'CAACAgEAAxkBAANHYfyZzlReI7eiTthQBujhH55NFCEAAtgCAAIDOJBGOtSSD5e3RocjBA'
     context.bot.send_sticker(
        chat_id=update.effective_chat.id, sticker=custom_sticker)

def jeffery(update, context):
    custom_stickers = [
      'CAACAgEAAxkBAANwYf7sozr66HDK5HcSCILk4dAQHpcAAkgCAAIQ5gABRY8RbPbDLgenIwQ',
      'CAACAgEAAxkBAANOYf7scEJMWrh8TMa3nzogdOBKupoAAq0BAAI1QchEa2GYXo5yhJYjBA',
      'CAACAgEAAxkBAANPYf7scqYZxmeRYD0tIcULwL1rfbYAArABAAKPk2lEtNMOH2T7V0EjBA',
      'CAACAgEAAxkBAANQYf7sdCRmk7Rme5aw61GAlNDW0Q0AAtoBAALr8WhEkA67tA2sUpYjBA',
      'CAACAgEAAxkBAANRYf7sdeL9pjn_GE6h3HacxcuhutsAAikCAAKRuWlEyb52TTv4Ej0jBA',
      'CAACAgEAAxkBAANSYf7sdw7NTq5Xq95fRKJn_ebC3dwAAtwBAAJjc2lEsdy3YrjpKfgjBA',
      'CAACAgEAAxkBAANTYf7sePciDkDUknz6mHgxNn8tFyMAAmoBAALU7mlEiDdp2xoC38wjBA',
      'CAACAgEAAxkBAANUYf7secDgoNUxIWIV2ikNVNcOr1cAAucBAAK7BmlEHT-fnRvXhkUjBA',
      'CAACAgEAAxkBAANVYf7sfO3PWS1Jv-JnrH1dvr0AAf2HAAIbAQAC9oIBRk19HrXjz127IwQ'      
    ]
    randomSticker = random.randint(0, len(custom_stickers)-1)
    context.bot.send_sticker(
    chat_id=update.effective_chat.id, sticker=custom_stickers[randomSticker]
)

def jewfery(update, context):
    custom_sticker = 'CAACAgEAAxkBAAPCYf8g69ymZ0KAB8O4UUHa4jRMaOwAAmkCAAIMbPBH5c2euHZDyPIjBA'
    context.bot.send_sticker(
        chat_id=update.effective_chat.id, sticker=custom_sticker)

def nicehat(update, context):
     custom_sticker = 'CAACAgEAAxkBAAEQtX9iAaxQHRcylsji9qe0rcCjCPJv6wACbgMAAjmpEURquuCk6ujzxSME'
     context.bot.send_sticker(
        chat_id=update.effective_chat.id, sticker=custom_sticker)

### GIFs ###        

def ackchyually(update, context):
    custom_gif = 'CgACAgEAAxkBAAMHYfb6yGuD6HExeYRQsHWB41yAUUgAAq8BAALP4FFHF64m5AcI2QwjBA'
    context.bot.send_animation(
        chat_id=update.effective_chat.id, animation=custom_gif
    )

def wojakindex(update, context):
    custom_gif = 'CgACAgEAAxkBAAMWYfb_pm9ih0ZfGZIMRVxHU13Bps8AAlECAAI66QABRa7QMnl58Mc0IwQ'
    context.bot.send_animation(
        chat_id=update.effective_chat.id, animation=custom_gif
    )


def chocofondant(update, context):
    custom_gif = 'CgACAgQAAxkBAAMcYfcDlBogULqhUW9v4ihAuevQjGoAAioDAAJyWbVSZoBZ-vFCcS0jBA'
    context.bot.send_animation(
        chat_id=update.effective_chat.id, animation=custom_gif
    )

def coom(update, context):
    custom_gif = 'CgACAgEAAxkBAAMdYfyR2MqaaFnN4jnnIZUjMb9IMq0AAnQCAAK2AAFgRzplq1TL2hbGIwQ'
    context.bot.send_animation(
        chat_id=update.effective_chat.id, animation=custom_gif
    )

def alwayshasbeen(update, context):
    custom_gif = 'CgACAgEAAxkBAAMgYfySVNQHn9Ov9UjnP3ebMIqfT3IAAlwBAAIJIRBHP-8Bqkcwwm4jBA'
    context.bot.send_animation(
    chat_id=update.effective_chat.id, animation=custom_gif
)

def moonman(update, context):
    custom_gifs = [
         'CgACAgEAAxkBAAMmYfyVKtrReI5iUqpKUOr3_oXj__kAAssBAAJRI9FHfdntlBaMPKEjBA', 'CgACAgEAAxkBAAMnYfyV_8gUm7xyzEDWclG2TeBVEWkAAoABAAI2BllHNO5reUOeZCYjBA', 'CgACAgQAAxkBAAM1YfyW1-UOIAmRcZZbL_y0o1zwaUIAAiMDAAI80MRSSLfj28XAXj8jBA']
    randomGif = random.randint(0, len(custom_gifs)-1)
    context.bot.send_animation(
    chat_id=update.effective_chat.id, animation=custom_gifs[randomGif]
)

def brrr(update, context):
    custom_gif = 'CgACAgEAAxkBAANDYfyXOojVEn5lfC87K-mBk_-YjNEAAiUCAAIM_vhHLu8UgdjyXwEjBA'
    context.bot.send_animation(
    chat_id=update.effective_chat.id, animation=custom_gif
)

def lamboshop(update, context):
    custom_gif = 'CgACAgIAAxkBAANGYfyXnkU9-UcYjX603HyoCqMpzb0AAloIAAIFZrhKS5HDe_HTxLYjBA'
    context.bot.send_animation(
    chat_id=update.effective_chat.id, animation=custom_gif
)

# Always have this object at the last line | Add your custom commands to this dict
custom_cmds = {
    'samsayingyes': samsayingyes,
    'ackchyually': ackchyually,
    'wojakindex': wojakindex,
    'jefferysayingyes': jefferysayingyes,
    'chocofondant': chocofondant,
    'coom': coom,
    'alwayshasbeen': alwayshasbeen,
    'moonman': moonman,
    'brrr': brrr,
    'lamboshop': lamboshop,
    'forcefulyes': forcefulyes,
    'jeffery': jeffery,
    'jewfery': jewfery,
    'nicehat': nicehat
}
