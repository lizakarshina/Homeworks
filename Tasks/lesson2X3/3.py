# Вивести на екран переклад "Hello World" на
# трьох різних мовах
from googletrans import Translator

ts = Translator()

ua = ts.translate("Записати у текстовий файл кілька рядків інформації англійською мовою та вивести на екран переклад цієї інформації українською", src='uk', dest='en')
pl = ts.translate("Hello World", src='en', dest='pl')
fr = ts.translate("Hello World", src='en', dest='fr')

print(f'''
      
      {ua.text}
      {pl.text}
      {fr.text}
      
      ''')