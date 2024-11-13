# Створіть функцію, яка приймає два числа — основу і показник степеня. 
# Функція повинна обчислити основу, піднесену до степеня, використовуючи цикл, і повернути результат.

def stepinb(osnova, pokaznik):
    result = 1
    i = 0
    
    while i < pokaznik:
        result *= osnova
        i += 1
        
    return result


print(stepinb(2, 3))
print(stepinb(5, 4))