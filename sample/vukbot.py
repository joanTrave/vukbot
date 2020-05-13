from __future__ import absolute_import
from typing import NoReturn
import logging

from telegram import Update, Message
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext

from commands.pole import pole_f
from commands.sol import sol_f
from setup.setup import BOT_TOKEN

UPDATER: Updater = Updater(token=BOT_TOKEN, use_context=True)
DISPATCHER: Dispatcher = UPDATER.dispatcher

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main() -> NoReturn:
    """
    Creates the updater and the dispatcher
    :return: Nothing
    """
    DISPATCHER.add_handler(CommandHandler('amanecer', sol_f))
    DISPATCHER.add_handler(MessageHandler(Filters.text & (~Filters.command), pole_f))
    UPDATER.start_polling()


if __name__ == '__main__':
    main()
