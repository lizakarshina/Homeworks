# Напишіть програму, яка приймає словник, та змінює всі значення 
# на їх квадрати.,

slovnik = {
    1: 1,
    2: 2,
    3: 3
}


for key, val in slovnik.items():
    slovnik[key] = val ** 3
    
print(slovnik)