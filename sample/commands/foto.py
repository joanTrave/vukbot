from telegram import Update, Message

from .utils.utils import get_random_photo_url, flip_coin


def foto_f(update: Update, context) -> Message:
    try:
        photo = get_random_photo_url(" ".join(context.args))
        return context.bot.send_photo(chat_id=update.effective_chat.id,
                                  photo=photo)
    except:
        return context.bot.send_message(chat_id=update.effective_chat.id,
                                  text="Lo siento :( No he encontrado nada")
    