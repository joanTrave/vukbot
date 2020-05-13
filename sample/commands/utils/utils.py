import datetime
import pytz
import os

import pandas as pd
import numpy as np

from astral import LocationInfo
from astral.sun import sun


POLES_PATH: str = os.path.dirname(os.path.abspath(__file__)) + '/poles.csv'


def get_sunrise() -> datetime.datetime:
    city = LocationInfo("Bigues i Riells", "Spain", "Europe/Madrid", 41.6833, 2.2333)
    s = sun(city.observer, date=datetime.date.today())
    return s["sunrise"] + datetime.timedelta(hours=2)


def get_user_winner(chat_id: int, day: datetime.date, user_id: int) -> bool:
    df: pd.DataFrame = pd.read_csv(POLES_PATH)
    df_winner = df[(df["chat_id"] == chat_id) & (df["day"] == day.strftime("%Y-%m-%d"))]
    if not df_winner["user_id"].count():
        df_result = pd.DataFrame(
            {
                "chat_id": [chat_id],
                "day": [day],
                "user_id": [user_id],
                "pole": [True]
            }
        )
        with open(POLES_PATH, 'a') as f:
            df_result.to_csv(f, header=False)
    return df_winner["user_id"].count() == 0
