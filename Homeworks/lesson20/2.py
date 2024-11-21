# Напишіть функцію, яка отримує шлях до файла і слово як аргументи.
# Функція повинна перевіряти, скільки разів слово зустрічається у файлі.


def count_words(path, word):
    count = 0
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        for slovo in line.split():
            
            if slovo == word:
                count += 1

    return count


print(
    count_words(
        "C:\\Users\\hayan\\Desktop\\прогламы\\Python\\Homeworks\\input.txt", "не"
    )
)
