import math
from datetime import datetime

# date = str("2024-09-01")
def get_days_from_today(date):
    date_now = datetime.now()
    
    try: #обробка помилок
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError as ve1:
    # print("ValueError", ve1)
        print("Невірний формат дати")

    try:
        get_days_from_today = abs(date_now.toordinal() - date.toordinal())
        print(get_days_from_today) 
        return get_days_from_today
        
        
    except NameError as ne1:
        print("NameError", ne1)
        
get_days_from_today("2024-09-16")
