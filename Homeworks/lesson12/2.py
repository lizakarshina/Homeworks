# Ознайомитись з методами:
# str = "abcd"
# random.choise(str)


import random

list = ["@", "!", "?", "."]


abetka = "abcdefghijklmnopqrstuvwxyz" # Add


pass_length = int(input("Введіть довжину паролю: "))
rand_number = random.randint(0, 99)


password = ""


for i in range(pass_length):

    litera = random.choice(abetka)

    randasdas = random.randint(0, 100)
    ran_number2 = random.randint(0, 100) # Add

    number = random.randint(0, rand_number)
    rand_char = random.randint(0, len(list) - 1)

    if randasdas > 50:
        if ran_number2 < 50: # Add
            if ran_number2 < 25: # Add
                password += litera.upper()
            else:
                password += litera
        else:
            password += str(list[rand_char])

    else:
        password += str(number)

print(f"Ваш пароль: {password}")
