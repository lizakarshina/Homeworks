# 2. Знайдіть найбільш довге слово у рядку без використання методів рядків.

def find_longest_word(text):
    longest = ''
    curr = []

    for char in text:
        print(curr)
        
        if char in ' .,?!':
            if len(curr) > len(longest):
                longest = ''.join(curr)
                
            curr = []
        else:
            curr.append(char)
                
    if len(curr) > len(longest):
        longest = ''.join(curr)
        
    return longest

print(find_longest_word('If you turn into an eggplant'))