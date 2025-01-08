slovnik = {}


print('Введіть вийти якщо хочете зупинитися\n')

while True:
    name = input('Введіть назву товару:\n')

    if name == 'вийти':
        break

    price = int(input('Введіть ціну товару\n'))

    slovnik[name] = price


summ = 0

for val in slovnik.values():
    summ += val

print(slovnik)
print(f'Загальна ціна всіх товарів: {summ}')