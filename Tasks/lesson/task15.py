list = [7, 11, 3, 4, 5, 6, 7, 8, 9, 10]

min = list[0]

for i in list:
    if i < min:
        min = i
    
print(min * 3)