
# Завдання 2: Напишіть програму, яка дозволяє користувачеві вводити 
# ім'я та академічні оцінки студентів у списки. 
# Після того, як користувач завершить введення даних, програма має вивести на екран:
# Список студентів разом з їхніми оцінками.
# Середню оцінку для кожного студента.
# Середню оцінку для всіх студентів.


students_list = []
avg_grade = 0
i = 1

print('Введіть "q" щоб завершити введеня студентів')

while True:
    
    student_name = input("Введіть Ім'я студента: ")
    if student_name == 'q':
        break
    
    student_grades = input('Введіть оінки студента (через пробіл): ').split()
    if student_grades == 'q':
        break
        
    
    avg_student_grade = 0
    for item in student_grades:
        item = int(item)
        avg_student_grade += item
        
    avg_student_grade /= len(student_grades)
    
    new_student = [student_name, student_grades, avg_student_grade]
    students_list.append(new_student)

if students_list:
    
    for item in students_list:
        print(f"{i}. Ім'я: {item[0]}\n     Оцінки: {item[1]}\n     Середній бал: {item[2]}")
        i += 1
        
    for item in students_list:
        avg_grade += item[2]
        avg_grade /= len(students_list)
    print(f'Середній бал всіх студентів: {avg_grade}')
else:
    print('Не введено жодного студента')