import datetime

from datetime import datetime
date_now = datetime.now()
date1 = str("0021-10-09")
# date1 = input("Введіть дату y форматі YYYY-MM-DD:   ")
try: #обробка помилок
    date = datetime.strptime(date1, "%Y-%m-%d")
except ValueError as ve1:
    # print("ValueError", ve1)
    print("Невірний формат дати")

def get_days_from_today(date):
    get_days_from_today = date_now.toordinal() - date.toordinal()
    print(get_days_from_today)
    return get_days_from_today

try: #обробка помилок
    get_days_from_today(date)
except NameError as ne1:
    print("NameError", ne1)

