# Написати програму, що виведе список, після видалення із нього непарних елементів

list = [1, 1, 1, 2, 2, 3, 3, 5, 255]

list2 = []

for item in list:
    if item % 2 == 0:
        list2.append(item)
    
print(list2)