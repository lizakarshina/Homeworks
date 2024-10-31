# Напишіть програму, яка приймає список рядків та повертає список, 
# в якому кожен елемент — це рядок, який містить першу літеру 
# кожного слова в вхідному рядку.

string = "Рядок. Кішка! Сир, Овочі."

string = string.replace('.', ' ')

list = ['!', '.', ',', '?']


for i in list:
    string = string.replace(i, ' ')
    
print(string.split())








# list_of_first_chars = []

# i = 0

# for char in string:
#     if char in list:
#         id = string.index(char)
        
#         list_of_first_chars.append(string[i:id]) 
        
#         i = id + 1
# print(list_of_first_chars)