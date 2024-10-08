first_list= []
second_list = []

while True:
    new_item = input('Введіть число: ')
    
    if new_item == 'Стоп':
        break
    else:
        new_item = int(new_item)
        first_list.append(new_item)

print(first_list)

for item in first_list:
    
    if item % 2 == 0:
        second_list.append(item)
        
print(first_list, '\n\n', second_list)