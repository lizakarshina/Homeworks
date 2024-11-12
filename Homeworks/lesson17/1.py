# Завдання 1
# Написати функцію, яка бронює столик у ресторані.
# В якості аргументів функції використати прізвище клієнта та кількість, час, день.
# Для другого параметру передбачити значення за замовчуванням — 2.

orders = {}

# name = input("Введіть ім'я\n")
# person_count = int(input("Введіть кількість людей"))
# time = input("На яку годину?\n")
# day = input("В який день?")


def create_order(name, day, time, count=2):
    global orders
    
    is_true = orders.get(name, -1)
    if is_true == -1:
        orders[name] = {
            0: {
                "id": 0,
                "clients": count,
                "day": day,
                "time": time,
            }
        }
    else:
        id = list(orders[name].keys())[-1]
        orders[name][id + 1] = {
            "id": id + 1,
            "clients": count,
            "day": day,
            "time": time,
        }

create_order("Олександр", "Четвер", "18:00", 2)
create_order("Олександр", "Четвер", "18:00", 4)

print(orders)
