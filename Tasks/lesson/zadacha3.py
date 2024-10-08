# клас Вчитель предмет, оцінка

class_number = input("В якому ти класі? ")
favourite_teacher = input("Хто твій улюблений вчитель? ")
favourite_predmet = input("Який в тебе найулюбленіший предмет? ")
grade = input(f"Яка в тебе оцінка за {favourite_predmet}? ")

info = "Я учень " + class_number + " класу.\nМій улюблений вчитель " + favourite_teacher + ", він веде " + favourite_predmet + ".\nУ мене з цього предмету: " + grade

print(info)