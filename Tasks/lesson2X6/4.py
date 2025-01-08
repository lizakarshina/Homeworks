list = [1, 2, 2, 3, 1, 2, 5, 6, 10, 22]
dict = {}

for item in list:

    if item not in dict.keys():
        dict[item] = list.count(item)
    else:
        continue


print(dict)