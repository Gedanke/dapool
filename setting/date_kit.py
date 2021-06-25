# -*- coding: utf-8 -*-


import time
import pandas
import datetime
import random
from dateutil.relativedelta import relativedelta

"""
time
"""


def quarter(month: str):
    """

    :param month:
    :return:
    """
    if month in {"1", "2", "3"}:
        return "1"
    elif month in {"4", "5", "6"}:
        return "2"
    elif month in {"7", "8", "9"}:
        return "3"
    elif month in {"10", "11", "12"}:
        return "4"
    else:
        return ""


def year_qua(date: str):
    """

    :param date:
    :return:
    """
    month = date[5:7]
    return [date[0:4], quarter(month)]


def get_today():
    """

    :return:
    """
    return str(datetime.datetime.today().date())


def get_year():
    """

    :return:
    """
    return datetime.datetime.today().year


def get_month():
    """

    :return:
    """
    return datetime.datetime.today().month


def get_hour():
    """

    :return:
    """
    return datetime.datetime.today().hour


def today_last_year():
    """

    :return:
    """
    return str(datetime.datetime.today().date() - relativedelta(years=1))


def day_last_week(days=-7):
    """

    :param days:
    :return:
    """
    return str(datetime.datetime.today().date() + datetime.timedelta(days))


def day_last_date(date, days=-1):
    """

    :param date:
    :param days:
    :return:
    """
    last = datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(days)
    return str(last)[0:10]


def get_now():
    """

    :return:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")


def int_time(timestamp):
    """

    :param timestamp:
    :return:
    """
    time_str = datetime.datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    return time_str


def diff_day(start=None, end=None):
    """

    :param start:
    :param end:
    :return:
    """
    day_start = datetime.datetime.strptime(start, "%Y-%m-%d")
    day_end = datetime.datetime.strptime(end, "%Y-%m-%d")
    return (day_end - day_start).days


def get_quarts(start: str, end: str):
    """

    :param start:
    :param end:
    :return:
    """
    idx = pandas.period_range(
        "Q".join(year_qua(start)), "Q".join(year_qua(end)), freq="Q-JAN"
    )
    return [str(d).split("Q") for d in idx][::-1]


def trade_cal():
    """

    :return:
    """
    return pandas.read_csv("http://file.tushare.org/tsdata/calAll.csv")


def is_holiday(date: str):
    """

    :param date:
    :return:
    """
    df = trade_cal()
    holiday = df[df.isOpen == 0]["calendarDate"].values
    today = ""
    if isinstance(date, str):
        today = datetime.datetime.strptime(date, "%Y-%m-%d")
    if today.isoweekday() in [6, 7] or str(date) in holiday:
        return True
    return False


def last_today_date():
    """

    :return:
    """
    today = int(datetime.datetime.today().date().strftime("%w"))
    if today == 0:
        return day_last_week(-2)
    return day_last_week(-1)


def tt_dates(start="", end=""):
    """

    :param start:
    :param end:
    :return:
    """
    dates = [
        d for d in range(int(start[0:4]), int(end[0:4]) + 1, 2)
    ]
    return dates


def _random(n=13):
    """

    :param n:
    :return:
    """
    return str(random.randint(10 ** (n - 1), (10 ** n) - 1))


def get_q_date(year=None, quarter=None):
    """

    :param year:
    :param quarter:
    :return:
    """
    dt = {
        "1": "-03-31", "2": "-06-30", "3": "-09-30", "4": "-12-31"
    }
    return "%s%s" % (str(year), dt[str(quarter)])
