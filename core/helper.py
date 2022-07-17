from time import strptime
import datetime

# Date format is YYYY-MM-DD
holidays = [
    "2022-01-26",
    "2022-03-18",
    "2022-04-15",
    "2022-05-03",
    "2022-08-15",
    "2022-08-31",
    "2022-09-09",
    "2022-10-05",
    "2022-10-24",
    "2022-10-25",
]


def is_holiday():
    date_holidays = [strptime(x, "%Y-%m-%d") for x in holidays]
    today = datetime.datetime.now().date().timetuple()
    is_date_found = False
    for each_holiday in date_holidays:
        if today == each_holiday:
            is_date_found = True
            break
    return is_date_found


def is_morning():
    return datetime.datetime.now().time() < datetime.time(12)


def is_login_button(text: str):
    return text.lower() == 'log in'
