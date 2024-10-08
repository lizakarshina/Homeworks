x = input('Введіть Х: ')
y = input('Введіть Y: ')

x = int(x)
y = int(y)

if x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x > 0 and y < 0:
    print('IIII')
else:
    print('I')