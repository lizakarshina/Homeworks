def add_item():
    while True:
        new_item = input('Введіть завдання: ')
        
        if new_item == 'q':
            break
        else:
            
            if new_item in todo_items:
                print('Вже є таке завдання')
            else:
                todo_items.append(new_item)
                
def print_items():
        
    i = 1
    for item in todo_items:
        print(f'{i}. {item}')
        i += 1

def remove_item():
    print_items()
    
    command = int(input('Введіть номер завдання: '))
    command -= 1
    
    if command in range(len(todo_items)):
    
        removed_item = todo_items.pop(command)
        completed_items.append(removed_item)
        print_items()
        
    else:
        print('Такого завдання не існує')
        
todo_items = []
completed_items = []

add_item()

while True:
    
    print('Список команд:')
    command = int(input('1. Видалити\n2. Додати\n3. Вихід\n'))

    if command in range(1, 4):
        
        if command == 1:
            remove_item()
        elif command == 2:
            add_item()
        else:
            break
    else:
        print('Такої команди не існує')