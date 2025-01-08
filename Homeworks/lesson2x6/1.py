# 1. Знайдіть кількість слів, що закінчуються на певну літеру.

def find_count_by_last_char(text, to_find):
    count = 0
    text = text.split()

    for word in text:
        if word[-1] in ',.?!':
            if word[-2] == to_find:
                count += 1
        else:
            if word[-1] == to_find:
                count += 1
    return count

print(find_count_by_last_char('Знайдіть кількість слів, що закінчуються на певну літеру.', 'ь'))