list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(list)):
    if i == 5 or i == 7 or i == 0:
        continue
    print(list[i])