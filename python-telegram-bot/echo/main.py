from telegram import Bot, ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from echo.config import TG_TOKEN


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Привет отправь мне что-нибудь"
    )


groupsArray = ['-1001268387954', '-1001172889341']


def do_echo(bot: Bot, update: Update):
    text = update.message.text
    print(update)
    print('Chat Id:', update.message.chat_id, update.message.chat.title)
    update.message.reply_to_message and print('Reply to message:', update.message.reply_to_message.text)
    if update.message.chat_id == 902120850 or update.message.chat_id == 380971860 or update.message.chat_id == 383288387:
        # publishing news only with #news hash tag
        if "#news" in text:
            for group in groupsArray:
                bot.send_message(
                    chat_id=group,
                    text=text
                )
        # reply to messages from groups
        elif update.message.chat_id == 902120850:
            for group in groupsArray:
                reply_chat_id = update.message.reply_to_message.text.split("\n")
                print(reply_chat_id)
                print(update.message.reply_to_message.message_id)
                if group == reply_chat_id[0]:
                    bot.send_message(
                        chat_id=group,
                        text=text
                    )
    elif "@janajayiqbot" in text:
        bot.send_message(
            chat_id=902120850,
            text='{}\n{}'.format(update.message.chat_id, text),
            groupId=update.message.chat_id
        )


def main():
    bot = Bot(
        token=TG_TOKEN
    )
    updater = Updater(
        bot=bot
    )
    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
