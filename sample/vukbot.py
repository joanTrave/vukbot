from typing import NoReturn
import logging

from telegram.ext import Updater, Dispatcher

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
    UPDATER = Updater(token='TOKEN', use_context=True)
    DISPATCHER = UPDATER.dispatcher


if __name__ == '__main__':
    main()
