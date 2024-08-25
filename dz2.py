import random
min = 93
max = 100

quantity = 1


def get_numbers_tickets(min, max, quantity):
    if min>0 and max<1000 and quantity<len(range(min,max)):
        a = list(range(min,max+1))
        get_numbers_tickets = random.sample(a, quantity)
        print(sorted(get_numbers_tickets))
        return get_numbers_tickets
    else:
        get_numbers_tickets = []
        print(sorted(get_numbers_tickets))
        return []
        
get_numbers_tickets(min, max, quantity)
get_numbers = get_numbers_tickets(1, 100, 5)
print(f"Ваші лотерейні числа:{sorted(get_numbers)}")

