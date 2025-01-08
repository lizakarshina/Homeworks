def change_symbol(text, a, b):
    answer = ''
    for char in text:
        if char != a:
            answer += char
        else:
            answer += b

    return answer

print(change_symbol("Якщо заплющити очі, стає темно", 'о', ':P'))