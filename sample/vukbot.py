from typing import NoReturn
import logging

from telegram.ext import Updater, Dispatcher

from setup.setup import BOT_TOKEN

UPDATER: Updater = None
DISPATCHER: Dispatcher = None

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main() -> NoReturn:
    """
    Creates the updater and the dispatcher
    :return: Nothing
    """
    global UPDATER, DISPATCHER
    UPDATER = Updater(token=BOT_TOKEN, use_context=True)
    DISPATCHER = UPDATER.dispatcher

    UPDATER.start_polling()


if __name__ == '__main__':
    main()
