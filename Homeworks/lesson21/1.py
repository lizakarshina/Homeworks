# Завдання 1: Напишіть програму, яка зчитує дані з текстового файлу, який містить список студентів і їх оцінок.
# Кожен рядок у файлі представляє окремого студента та його оцінки, розділені комою.
# Після зчитування файлу, програма повинна обчислити середній бал кожного студента і записати результат у новий файл з ім'ям "результати.txt".

result = []


with open("hw students1.txt", "r") as file:
    students = []
    for line in file:
        student = line.split(",")

        students.append(student)


for student in students:
    i = 1
    summ = 0
    while i != len(student):

        if "\n" in student[i]:
            student[i] = student[i][0:-1]

        num = int(student[i])
        summ += num

        i += 1
    result_str = f"{student[0]},{summ / i}\n"

    result.append(result_str)


with open("result.txt", "w") as file:
    file.writelines(result)
