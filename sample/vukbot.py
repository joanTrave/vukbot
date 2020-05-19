from __future__ import absolute_import
from typing import NoReturn
import logging

from telegram import Update, Message
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext

from commands.pole import pole_f
from commands.sol import sol_f
from commands.chocolate import chocolate_f
from commands.foto import foto_f
from commands.fascista import fascista_f
from setup.setup import BOT_TOKEN, PEXELS_API_KEY
from commands.utils.utils import set_up_api

UPDATER: Updater = Updater(token=BOT_TOKEN, use_context=True)
DISPATCHER: Dispatcher = UPDATER.dispatcher

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(update: Update, context: CallbackContext) -> Message:
    print(update.message.text)
    return context.bot.send_message(chat_id=update.effective_chat.id, text=str(type(context)))


def main() -> NoReturn:
    """
    Creates the updater and the dispatcher
    :return: Nothing
    """
    set_up_api(PEXELS_API_KEY)
    DISPATCHER.add_handler(CommandHandler('amanecer', sol_f))
    DISPATCHER.add_handler(CommandHandler('chocolate', chocolate_f))
    DISPATCHER.add_handler(CommandHandler('foto', foto_f))
    DISPATCHER.add_handler(MessageHandler(Filters.text & (~Filters.command), pole_f))
    # DISPATCHER.add_handler(MessageHandler(Filters.text & (~Filters.command), fascista_f))
    UPDATER.start_polling()


if __name__ == '__main__':
    main()
