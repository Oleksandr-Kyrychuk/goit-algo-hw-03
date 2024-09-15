from datetime import datetime

# date = str("2024-09-01")
def get_days_from_today(date):
    date_now = datetime.now()
    
    try: #обробка помилок
        date = datetime.strptime(date, "%Y-%m-%d")
        get_days_from_today = date_now.toordinal() - date.toordinal()
        return get_days_from_today
    except ValueError as ve1:
    # print("ValueError", ve1)
        print("Невірний формат дати")
        return
        
# get_days_from_today("2024-09-16")
result = get_days_from_today("2024-09-16")
if result != None:
    print(f"Кількість днів: {result}")
