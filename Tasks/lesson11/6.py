# Створити програму, яка приймає список чисел та повертає список елементів, які є менші за середнє значення списку.

import random

list = []
sum = 0

while len(list) < 15:
    list.append(random.randint(1, 1))

for item in list:
    sum += item

mid = sum / len(list)
print(list)
print(mid)
