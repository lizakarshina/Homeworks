
# Записати у текстовий файл кілька рядків інформації
# англійською мовою та вивести на екран переклад цієї
# інформації українською
from googletrans import Translator

ts = Translator()

with open('translate.txt', 'r') as file:
    lines = file.readlines()

translated = ''
for line in lines:
    translated += ts.translate(line, src='en', dest='uk').text + '\n'

print(translated)
