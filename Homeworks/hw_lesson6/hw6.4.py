# + Вигадати спосіб вивести все в один рядок до завдання, яке було сьогодні останнім (фрукти та останній фрукт).

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'orange']
last_fruit = fruits.pop()

str_of_fruits= ''
for item in fruits:
    str_of_fruits += f'{item} '

print(last_fruit + '- видалений фрукт\n' + str_of_fruits + '- фрукти, що залишилися')

