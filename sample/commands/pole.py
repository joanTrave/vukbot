import datetime
import pytz

from telegram import Update, Message

from sample.commands.utils.utils import get_sunrise, get_user_winner


utc=pytz.UTC


def pole_f(update: Update, context) -> Message:
    if update.message.text.lower() not in {"pole", "plata", "bronce"}:
        return context.bot.send_message
    sunrise: datetime.datetime = get_sunrise()
    now: datetime.datetime = datetime.datetime.now() + datetime.timedelta(hours=2)

    pole: bool = now.replace(tzinfo=utc) > sunrise.replace(tzinfo=utc)
    if pole:
        if get_user_winner(update.effective_chat.id, datetime.date.today(), update.effective_user.id):
            text = f"Felicidades {update.effective_user.first_name}, has hecho la pole mañanera"
            return context.bot.send_message(chat_id=update.effective_chat.id, text=text)
