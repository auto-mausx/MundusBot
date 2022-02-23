# MundusBot script #
from ctypes import util
import os
import http
from flask import Flask, request
from telegram import Bot, Update
from werkzeug.wrappers import Response
from lib import utilities
from lib import mundusfuncs
# Always import custom just in case, even if file is empty
from lib import custom
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
version = 2.0  # BLOOD

# == Global Variables ==#

app = Flask(__name__)
bot = Bot(token=os.environ["BOT_TOKEN"])

# Connection to Database
# db = utilities.returnSetting('server_database')
# db_connection = utilities.create_connection(db)

# Telegram Chat Token #
token = os.environ.get("BOT_TOKEN")
# Updater Object #
updater = Updater(token, use_context=True)
# Dispatcher #
dispatcher = updater.dispatcher

# ===== Commands =====#

# Help
def getHelp(update, context):
    # telegram_msg = utilities.catchDebug(mundusfuncs.fetchHelp())
    telegram_msg = """Current list of commands:\n
                        '/samsayingyes'\n
                        '/ackchyually'\n
                        '/wojakindex'\n
                        '/jefferysayingyes'\n
                        '/chocofondant'\n
                        '/coom'\n
                        '/alwayshasbeen'\n
                        '/moonman'\n
                        '/brrr'\n
                        '/lamboshop'\n
                        '/forcefulyes'\n
                        '/jeffery'\n
                        '/jewfery'\n
                        '/getwojakindex'\n
                        '/nicehat'\n
                        '/jeetrug',\n
                        '/goingtozero'
                    """

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=(telegram_msg)
    )

# Get Gas


def getGas(update, context):
    gas_result = utilities.catchDebug(mundusfuncs.returnGas())

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=(gas_result))

# Wojak index
def getwojakIndex(update, context):
    wojak_index = utilities.catchDebug(mundusfuncs.getwojakInx())

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=(wojak_index)
    )


# Unknown Command
def unknownCmd(update, context):
    response = 'Sorry, I didn\'t understand that command. Try /gethelp to see a list of commands'
    if update.message.text == "/p":
        return
    else:    
        update.message.reply_text(text=response)


# ===== Admin Commands ===== #



# ===== Handlers ===== #
# Command Dictionary is always filled with default commands
command_dict = {
    'gethelp': getHelp,
    'gas': getGas,
    'getwojakindex': getwojakIndex,
}
# Pulls the custom functions written by the user in ./lib/custom.py
if (utilities.returnSetting('custom_functions')):
    for key in custom.custom_cmds:
        command_dict[key] = custom.custom_cmds[key]

# Dispatch all commands found in the dictionary
for key in command_dict:
    try:
        print(f'Passing {key} to dispatcher')
        cmd = CommandHandler(key, command_dict[key])
        dispatcher.add_handler(cmd)
    except Exception as e:
        print(f'Something happened!{e}')


# Dispatch misc cmd handler seperately
dispatcher.add_handler(MessageHandler(Filters.command, unknownCmd))

# End of Line

@app.post("/")
def index() -> Response:
    dispatcher.process_update(Update.de_json(request.get_json(force=True), bot))
    return "", http.HTTPStatus.NO_CONTENT

# if __name__ == "__main__":
#     PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080

#     # This is used when running locally. Gunicorn is used to run the
#     # application on Cloud Run. See entrypoint in Dockerfile.
#     app.run(host="127.0.0.1", port=PORT, debug=True)


# updater.start_polling()
# updater.start_webhook(listen="0.0.0.0", port=int(os.environ.get('PORT', 8080)), webhook_url='https://mundus-bot-geeecxekiq-uc.a.run.app')
# updater.bot.set_webhook('https://mundus-bot-geeecxekiq-uc.a.run.app')
# updater.idle()