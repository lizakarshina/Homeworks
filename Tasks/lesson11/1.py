# Написати програму, що рахує суму всіх елеметів у списку.

list = [int(i) for i in range(1, 256, 17)]

sum = 1

for item in list:
    sum *= item
    
print(sum)