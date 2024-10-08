while True:
    a = int(input("Введіть число: "))
    
    if a < 20:
        continue
    
    if a > 100:
        break
    
    print(a)