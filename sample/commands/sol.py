import datetime

from telegram import Update, Message

from .utils.utils import get_sunrise


def sol_f(update: Update, context) -> Message:
    sunrise: datetime.datetime = get_sunrise()
    text: str = f"En Bigues i Riells, el dia {sunrise.strftime('%d-%m-%Y')} " \
                f"amanece a las {sunrise.strftime('%H:%M:%S')}"
    return context.bot.send_message(chat_id=update.effective_chat.id, text=text)
