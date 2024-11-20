# Напишіть програму, яка зчитує вміст файлу "input.txt" 
# і записує його у файл "output.txt" з виключенням повторюваних рядків.

lines_to_write = []
with open('input.txt', 'r', encoding='utf-8') as input:
    for line in input:
        lines_to_write.append(line)
        
lines_to_write2 = []

for line in lines_to_write:
    if line in lines_to_write2:
        continue
    else:
        lines_to_write2.append(line)

print(lines_to_write)
print(lines_to_write2)

with open('output.txt', 'w', encoding='utf-8') as output:
    output.writelines(lines_to_write2)