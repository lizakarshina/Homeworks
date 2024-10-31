# Гра "Вгадай слово". У цій грі комп'ютер загадує слово,
# а користувач повинен відгадати його, отримуючи на кожну
# спробу підказку від програми. Наприклад, на першій спробі
# програма може вивести довжину слова, на другій — першу букву
# слова, на третій — останню букву і т.д.

import random

# Список слів для гри

words = {
    "яблуко": {
        "first_letter": "я",
        "last_letter": "о",
    },
    "банан": {
        "first_letter": "б",
        "last_letter": "н",
    },
    "апельсин": {
        "first_letter": "а",
        "last_letter": "н",
    },
    "груша": {
        "first_letter": "г",
        "last_letter": "а",
    },
    "слива": {
        "first_letter": "с",
        "last_letter": "а",
    },
    "черешня": {
        "first_letter": "ч",
        "last_letter": "я",
    },
}

# Вибір випадкового слова
words_keys = [word for word in words.keys()]


word = 'банан'
attempts = 0  # Лічильник спроб


word_lenght = len(word)
first_letter = words[word]["first_letter"]
last_letter = words[word]["last_letter"]
random_letter = random.choice(word)


while random_letter == first_letter or random_letter == last_letter:
    random_letter = random.choice(word)


print("Комп'ютер загадав слово (їжа). Спробуйте його відгадати!")

# Основний ігровий цикл
while True:
    guess = input("Ваш варіант: ").strip().lower()
    attempts += 1

    # Перевірка відповіді
    if guess == word:
        print(f"Вітаємо! Ви вгадали слово '{word}' за {attempts} спроби.")
        break
    else:
        # Виведення підказок залежно від кількості спроб
        if attempts == 1:
            print(f"Підказка 1: Довжина слова - {word_lenght} символів.")
        elif attempts == 2:
            print(f"Підказка 2: Перша буква слова - '{first_letter}'.")
        elif attempts == 3:
            print(f"Підказка 3: Остання буква слова - '{last_letter}'.")
        elif attempts == 4:
            print(f"Підказка 4: Слово містить літеру '{random_letter}'.")
        else:
            print("Неправильно. Спробуйте ще раз!")
