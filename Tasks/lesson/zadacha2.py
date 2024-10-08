name = input("Як вас звати: ")
pan_or_pani = input("Як до вас звертитись? (Пан чи Пані) ")

if pan_or_pani == "Пані":
    print(f"Добрий день, пані {name}")
elif pan_or_pani == "Пан":
    print(f"Добрий день, пан {name}")
else:
    print("Некоректні дані")
    