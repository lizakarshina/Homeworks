numbers = [int(i) for i in input().split()]

i = 0
sum = 0

for number in numbers:
    
    if i < 5:
        sum += number
        i += 1
    else:
        break
    
print(sum)