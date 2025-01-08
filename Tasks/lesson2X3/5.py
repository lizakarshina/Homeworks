from googletrans import Translator

tr = Translator()

with open('boo.txt', 'w', encoding='utf-8') as file:
    file.writelines(['ЗСУ\n', "Україна\n", "понад усе\n"])

with open('boo.txt', 'r', encoding='utf-8') as boo:
    lines = boo.readlines()
    
    
translated = []
for line in lines:
    translated.append(tr.translate(line, src='uk', dest='en').text + '\n')
    
print(translated)
    
with open('boo_translated.txt', 'w') as boo2:
    boo2.writelines(translated)