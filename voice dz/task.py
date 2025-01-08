from googletrans import Translator

tr = Translator()

text = ''

with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        text += line


print(tr.translate(text, dest='en', src='uk').text)
