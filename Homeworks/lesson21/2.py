# Завдання 2: Напишіть програму, яка зчитує дані з текстового файлу, який містить імена та вік студентів.
# Кожен рядок у файлі містить ім'я студента та його вік, розділені комою.
# Після зчитування файлу, програма повинна знайти найстаршого та наймолодшого студентів і вивести їх імена на екран.

# Текстовий файл:
# John,20
# Alice,22
# Michael,18
students = []

with open('hw students2.txt', 'r') as file:
    for line in file:
        if '\n' in line:
            line = line[0:-1]
        students.append(line.split(','))
        
for student in students:
    student[1] = int(student[1])    
        

students = sorted(students, key=lambda student: student[1], reverse=True)


print(f'Найстарший: {students[0]}\nНаймолодший: {students[-1]}')