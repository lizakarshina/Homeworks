# Створіть функцію, яка приймає список слів і повертає найбільше слово за кількістю літер.
list = ["Літера", "Абетка", "Туберкульоз"]


def return_max(list):
    max = ""

    for word in list:
        if len(word) > len(max):
            max = word

    return max


print(return_max(list))
