
# result = dict(sorted(result.items(), key=lambda item item[1], reverse=True))


# Функції вверху 
# Визов функції внизу


# Аргументам у функціях можно задати дефолтне значення
# Якщо є дефолтне значення, то не треба його вказувати коли викликаєш функці.

# def func(a, b=5, c=10):
    # print(a, b, c)
    
    
# func(3)

# func(3, c=24)


# Змінюванне число параметрів
# аргументи забирають що можуть забрати?

# def total(a=5, *numbers, **phone_book):
#    print('a', a)
# # проходимо по всім елементам кортежа
#    for single_item in numbers:
#        print('single_item', single_item)
# # проходимо по всім елементам словника
#    for first_part, second_part in phone_book.items():
#        print(first_part,second_part)
# print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))