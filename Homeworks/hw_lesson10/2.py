# 2. Вигадати задачку з усіма методами множин та усіма математичними діями та вирішити її.
# Задачка має бути на якусь тему (наприклад, склад або комп'ютерний магазин)
# 'Dell', 'Apple', 'Acer'

notebooks = {'Lenovo', 'HP', }
monitors = {'Dell', 'Samsung', 'LG', 'Acer', 'BenQ'}
accessories = {'Мишка', 'Клавіатура', 'Чохол', 'Apple'}
other = {'Принтер', 'Сканер', 'Мишка', 'Dell', 'HP'}

# Add
notebooks.add('Dell')
notebooks.add('Apple')
notebooks.add('Acer')
monitors.add('AOC')
accessories.add('USB HUB')


# Remove

accessories.remove('USB HUB')
other.remove('Принтер')

# discard
notebooks.discard('Xiaomi')
notebooks.discard('AOC')


# Знайти та вивести всі елементи
all_items = notebooks | monitors | accessories | other
print(f'Всі елементи:\n{all_items}\n')


# Спільні елементи між notebooks та monitors
spilni = notebooks & monitors
print(f'Спільні елементи між notebooks та monitors:\n{spilni}\n')

# Не мпільні елементи між accessories та other, тобно всі окрім мишки
ne_spilni = accessories ^ other
print(f'Не спільні елементи між accessories та other:\n{ne_spilni}\n')