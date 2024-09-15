import random
min = 1
max = 5

quantity = 5


def get_numbers_ticket(min, max, quantity):
    if min>0 and max<1000 and quantity<=len(range(min,max+1)):
        a = list(range(min,max+1))
        get_numbers_ticket = random.sample(a, quantity)
        return sorted(get_numbers_ticket)
    else:
        get_numbers_ticket = []
        print(sorted(get_numbers_ticket))
        return []
        

get_numbers = get_numbers_ticket(min,max,quantity)
print(f"Ваші лотерейні числа:{get_numbers}")
