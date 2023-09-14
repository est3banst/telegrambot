
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6157329244:AAHTHFna_gkb_x6GbvAQNsA-f-AD6UyrmjY'
BOT_USERNAME: Final = '@overtaken_bot'


async def greet_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Thank you for reaching out, i'm a simple telegram bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Try anything and i will do my best to answer you but i can't do many things")

async def intro_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a bot made by: Esteban Mart. Bots can be a very useful tool to manage repetitive task, such as customer service")

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a basic bot made by a developer named: Esteban Mart, you can connect with him via email"
                                    " at: steven_devs@hotmail.com")

#Handling responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return "Hello there!"

    if 'how are you' in processed:
        return "I'm good i hope you're too"

    if 'who are you' or 'say something' in processed:
        return ("I'm a very basic bot that can handle a few responses and i was basically made"
                " to help you to connect with a developer")

    return "Try something else, i can't process what you just wrote"


#
async def hand_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot: ', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    print("Starting the bot")
    #Commands of the bot
    app.add_handler((CommandHandler('greetings', greet_command)))
    app.add_handler((CommandHandler('help', help_command)))
    app.add_handler((CommandHandler('intro', intro_command)))
    app.add_handler((CommandHandler('contact', contact_command)))

    #Messages received
    app.add_handler(MessageHandler(filters.TEXT, hand_message))

    #Error handler
    app.add_error_handler(error)

    print("Is polling..")
    app.run_polling(poll_interval=5)




