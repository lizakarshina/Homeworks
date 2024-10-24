dict = {1: '1', 2: 'dwa', 8: 'Серпень'}

str = '31.08.2024'
list = str.split('.')

month = 0

if int(list[1][0]) == 0:
    month = int(list[1][1])
else:
    month = int(list[1])
    
value = dict.get(month, -1)
print(month)
print(value)