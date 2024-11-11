# Завдання 1
# Написати функцію, яка бронює столик у ресторані.
# В якості аргументів функції використати прізвище клієнта та кількість, час, день.
# Для другого параметру передбачити значення за замовчуванням — 2.

orders = {}

# name = input("Введіть ім'я\n")
# person_count = int(input("Введіть кількість людей"))
# time = input("На яку годину?\n")
# day = input("В який день?")


def create_order(dict, name, day, time, count=2):
    is_true = dict.get(name, -1)

    if is_true == -1:
        dict[name] = {
            0: {
                "id": 0,
                "clients": count,
                "day": day,
                "time": time,
            }
        }
    else:
        id = list(dict[name].keys())[-1]
        dict[name][id + 1] = {
            "id": id + 1,
            "clients": count,
            "day": day,
            "time": time,
        }
    print("Done")


create_order(orders, "Олександр", "Четвер", "18:00", 2)
create_order(orders, "Олександр", "Четвер", "18:00", 4)

print(orders)
