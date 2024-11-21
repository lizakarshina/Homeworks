# Міні-проєкт. Робота з файлами
# Написати програму для зберігання та керування списком покупок.
# Основна ідея полягає в тому, щоб програма зберігала дані про
# список продуктів та їх кількість у текстовому файлі. Кожен рядок
# в файлі містить інформацію про один продукт та його кількість у
# форматі "назва продукту, кількість".
# Після запуску програми користувач може додавати нові продукти
# до списку та їх кількість, переглядати список, редагувати наявну
# інформацію, видаляти продукти зі списку та зберігати зміни у файлі.

list = []





def get_products():
    try:
        file = open('Product List.txt', 'r', encoding='utf-8')
        
        for line in file:
            list.append(line)
            
        file.close()
    except FileNotFoundError:
        file = open('Product List.txt', 'w')
        file.close()
        
        
def add_products():
    global list
    with open("Product List.txt", "w", encoding="utf-8") as file:
        
        for product in list:
            
            file.write(f'{product}\n')

    print("Було додано до списку\n")


def delete_product(id):
    global list
    list.pop(id)
    add_products()

def print_products():
    global list
    i = 1
    for product in list:
        
        print(f'{i}. {product}\n')
        i += 1

def change(id, new_data):
    global list
    list[id] = new_data
    add_products()
    
    
get_products()

while True:
    menu = int(input(
    """
    1. Додати
    2. Видалити
    3. Змінити
    4. Відобразити
    5. Вийти
    """))
    
    if menu in range(1, 6):
        if menu == 1:
            while True: 
                
                quit = input('Щоб продовжити натисніть Ентер, щоб закінчити введіть q\n')
                
                if quit == 'q':
                    break
                
                new_product = input('Введіть назву та кількість через кому\n')
                list.append(new_product)
            add_products()
            
        if menu == 2:
            print_products()
            
            index = int(input('Введіть номер продукту\n')) - 1
            while index not in range(len(list)):
                print('Ви ввели неправильний номер\n')
                index = int(input('Введіть номер продукту\n')) - 1

            delete_product(index)
            
        if menu == 3:
            print_products()
            
            index = int(input('Введіть номер продукту\n')) - 1
            new_data = input('Введіть назву та кількість через кому\n')
            
            while index not in range(len(list)):
                print('Ви ввели неправильний номер\n')
                index = int(input('Введіть номер продукту\n')) - 1
                
            change(index, new_data)
            
        if menu == 4:
            print_products()
            
        if menu == 5:
            break