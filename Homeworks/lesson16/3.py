# Крок 3. Створіть програму, яка приймає список рядків і повертає найчастіші 10 слів у цих рядках,
# ігноруючи звичайні займенники, прийменники та частки мови.


stop_slova = set(
    [
        "я",
        "ти",
        "він",
        "вона",
        "воно",
        "ми",
        "ви",
        "вони",
        "це",
        "його",
        "її",
        "та",
        "але",
        "або",
        "і",
        "й",
        "на",
        "у",
        "з",
        "за",
        "до",
        "по",
        "перед",
        "про",
        "як",
        "в",
        "до",
        "що",
        "чи",
        "так",
        "же",
        "би",
        "і",
    ]
)

lines = [
    "Це приклад тексту для тестування програми",
    "Програма має знайти найбільш часті слова і програми повернути їх",
]

dictionary = {}

for line in lines:

    words = line.lower().split()

    for word in words:
        if word not in stop_slova:
            if word in dictionary:
                dictionary[word] += 1

            else:
                dictionary[word] = 1
        else:
            continue

top_10 = []
dictionary_copy = dictionary.copy()
for i in range(10):
    top_word = ""
    top_val = 0

    for key, val in dictionary_copy.items():
        if val > top_val:
            top_val = val
            top_word = key

        if top_word:
            top_10.append([top_word, top_val])
            if top_word in dictionary_copy:
                
                del dictionary_copy[top_word]

print(top_10)
