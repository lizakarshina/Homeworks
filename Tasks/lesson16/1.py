# Створити програму обліку працівників у компанії. Основні компоненти: Додати працівника, Видалити працівника, 
# Переглянути список працівників, Змінити заробітну плату працівника.

workers = {
    'Єлизавета': {
        'name': 'Єлизавета',
        'salary': 1298371289,
        'position': 'Вчитель'
    },
    'Олександр': {
        'name': 'Олександр',
        'salary': 32323,
        'position': 'Студент'
        
    },
}

def add(dict, name, salary, position):
    new_dict = {
        'name': name,
        'salary': salary,
        'position': position
    }
    dict[name] = new_dict
    print(f'Ви додали працівника: {new_dict['name']}\nЗарплтня: {new_dict['salary']}\n Позиція: {new_dict['position']}')
    
def delete(dict, name):
    deleted = dict.pop(name)
    
    print(f'Ви видалили працівника: {deleted['name']}')
    

def change_salary(dict, name, new_salary):
    
    if dict:
    
        dict[name]['salary'] = new_salary
        print(f'Нова заралатня: {new_salary}')
    else:
        print('У вас ніхто не працює')
    
def list_all(dict):
    if dict:
        for key, val in dict.items():
            print(f'''
                Ім'я: {key}
                Зарплатня: {val['salary']}
                Позиція: {val['position']}
                ''')
    else:
        print('У вас ніхто не працює')
        
        
def change_position(dict, name, new_position):
    
    dict[name]['position'] = new_position
    
    print(f'Змінено позицію працівника {dict[name]['name']} на {new_position}')
        
while True:
    command = int(input('1. Додати\n2. Видалити\n3. Змінити зарплатню\n4. Показати всіх працівників\n5. Змінити позицію\n6. Вийти з програми\n'))
    
    if command in range(1, 6):
        if command == 1:
            name = input("Введіть ім'я\n")
            salary = int(input('Введіть зарплатню\n'))
            add(workers, name, salary)
            
        if command == 2:
            name = input("Введіть ім'я\n")
            
            delete(workers, name)
            
        if command == 3:
            name = input("Введіть ім'я\n")
            new_salary = int(input('Введіть нову зарплатню'))
            
            change_salary(workers, name, new_salary)
            
        if command == 4:
            list_all(workers)
            
        if command == 5:
            list_all(workers)
            
            worker_name = input("Ім'я працівника:\n")
            worker_position = input('Нова позиція:\n')
            change_position(workers, worker_name, worker_position)
        if command == 6:
            break
    else:
        print('Команди не існує')