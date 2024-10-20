# Створіть програму, яка приймає від користувача строку
# та перетворює її у список, де кожен елемент — це слово зі строки. Виведіть цей список.


str = input("Введіть рядок:\n")

list = list(str)
list_of_denied_chars = [',', '.', '?', '!']
new_list = []

for item in list:
    if item not in list_of_denied_chars:
        new_list.append(item)
      
new_list = ''.join(new_list).split()


print(new_list)