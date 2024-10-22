# Потрібно написати програму, яка приймає рядок від користувача та перевіряє чи є у рядку хоча б одна група символів, 
# що повторюється не менше як 2 рази. У результаті виводить ці групи у довільному форматі.


str = input('Введіть рядок:\n')
list = []


for i in range(0, len(str)):
    
    for j in range(i + 1, len(str)):
        
        zriz1 = str[i:j]
        zriz2 = str[j:]
        
        if zriz1 in zriz2:
            list.append(zriz1)
            
            
set = set(list)

print(set)