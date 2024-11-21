# Реалізуйте програму, яка зчитує вміст кількох файлів і об'єднує їх у новий файл "combined.txt".


lines = []
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lines.append(line)

with open('output.txt', 'r', encoding='utf-8') as file2:
    for line in file2:
        lines.append(line)

with open('combined.txt', 'a', encoding='utf-8') as combined:
    combined.writelines(lines)