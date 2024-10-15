# Скласти програму, яка буде рахувати, яка літера найчастіше зустрічається у вашому прізвищі.

last_name = 'Каршина'

last_name = last_name.lower()

max_count = 0
most_frequent_letter = ''

for letter in last_name:
    
        count = 0
        
        for char in last_name:
            
            if char == letter:
                count += 1
                
        if count > max_count:
            
            max_count = count
            most_frequent_letter = letter

print(f'Найчастіше зустрічається "{most_frequent_letter}" вона повторювалася: {max_count}')
