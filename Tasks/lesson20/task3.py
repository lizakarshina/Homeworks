# Реалізуйте програму, яка зчитує вміст файла "data.txt" і виводить кількість слів у цьому файлі.
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
count = 0
for line in lines:
    for word in line:
        if word in ' ,.!?\n':
            count += 1

    
print(count)
