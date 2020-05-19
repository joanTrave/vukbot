from telegram import Update, Message

from .utils.utils import get_random_photo_url


def chocolate_f(update: Update, context) -> Message:
    return context.bot.send_photo(chat_id=update.effective_chat.id,
                                  photo=get_random_photo_url('chocolate'))