from telegram import Update, Message

from .utils.utils import flip_coin


def fascista_f(update: Update, context) -> Message:
    a = flip_coin(3)
    print(a)
    if flip_coin(3):
        print("A")
        #update.message.reply_text("Fascista")