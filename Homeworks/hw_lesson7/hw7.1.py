# Завдання 1: Напишіть програму, яка дозволяє користувачеві ввести декілька речень (текст) і обробити цей текст. Після того, як користувач введе текст, програма має вивести на екран:
# Загальну кількість символів у тексті (включаючи пробіли).
# Кількість слів у тексті.
# Кількість речень у тексті.
# Загальну кількість унікальних слів (без урахування регістру).
# Список унікальних слів.

text = input('Введіть текст:\n')
list_of_uniques = []

words = text.split()
sentences = text.split('.')

for item in words:
    
    if item in list_of_uniques:
        list_of_uniques.remove(item)
    else:
        list_of_uniques.append(item)
        
        
number_of_chars = len(text)
number_of_words = len(words)
number_of_sentences = len(sentences)
number_of_uniques = len(list_of_uniques)

print(f'Кількість символів: {number_of_chars}')
print(f'Кількість слів: {number_of_words}')
print(f'Кількість речень: {number_of_sentences}')
print(f'Кількість унікальних слів: {number_of_uniques}')
print(f'Список унікальних слів:\n{list_of_uniques}')