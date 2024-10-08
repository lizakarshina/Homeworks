# Завдання 1
# Написати програму визначення координатної чверті.
# Перевіряючи спочатку координату «Y»
# (подумати як зробити все через 3 if else)


x = input("X: ")
y = input("Y: ")



x = int(x)
y = int(y)


if (y > 0 and x > 0) or (y == 0 and x == 0):

    print("I")
else:

    if y > 0 and x < 0:

        print("II")
    else:

        if y < 0 and x < 0:

            print("III")
        else:
            
            print("IV")

