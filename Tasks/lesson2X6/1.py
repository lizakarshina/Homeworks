

def is_anagrama(text1, text2):

    answer = False

    text1 = sorted(text1)
    text2 = sorted(text2)

    answer = text1 == text2

    return answer

print(is_anagrama('blah', 'blah'))