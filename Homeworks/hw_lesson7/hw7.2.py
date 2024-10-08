# Завдання 3:
# Напишіть програму, яка дозволяє керувати складом товарів.
# Користувач може додавати нові товари
# видаляти товари
# переглядати список наявних товарів
# знаходити товар за назвою 
# визначати загальну вартість товарів на складі.
items_list = [['Пепсі Манго', 159], ['Пепсі Зеро', 50], ['Пепсі Класік', 40]]
command_list = ['Додати товар', 'Видалити товар', 'Переглянути товари', 'Пошук за назвою', 'Розрахувати вартість всіх товарів', 'Вийти з програми']

print('Ку! Тут ти можеш керувати складом')

while True:
    print('Список команд:')
    k = 1
    for item in command_list:
        print(f'{k}. {item}')    
        k += 1
    command = int(input('Введіть номер команди: '))
    if command in range(1, 7):
        if command == 1:
            print()
            new_item_name = input('Введіть назву товару\n')
            new_item_price = int(input('Введіть ціну товару\n'))
            
            new_item = [new_item_name, new_item_price]
            
            items_list.append(new_item)
            print()
        if command == 2:
            print()
            i = 1
            for item in items_list:
                print(f'{i}. {item[0]}, {item[1]} грн.')
                i += 1
            id = int(input('Напишіть номер товару'))
            items_list.pop(id - 1)
            print()
        if command == 3:
            print()
            print('Список товарів:')
            i = 1
            
            for item in items_list:
                print(f'{i}. {item[0]}, {item[1]} грн.')
                i += 1
                
            print()
        if command == 4:
            print()
            search = input('Введіть назву товару: \n')
            
            for item in items_list:
                if search == item[0]:
                    print(item)
            
            print()
        if command == 5:
            print()
            sum = 0
            i = 0
            
            for item in items_list:
                sum += item[1]
            print(f'Вартість всіх товарів: {sum}')
            print()
        if command == 6:
            break
        print()
    else:
        print('Некоректна команда\n')