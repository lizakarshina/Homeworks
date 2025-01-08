from googletrans import Translator


with open('2.csv', 'a') as csv:
    
    csv.write('#3;1;2;3\n')
    
    # lines = csv.readlines()

# print(lines)

# мови: uk - українська, en - англійська,
# fr -французька, pl - польська, es - іспанська


translator = Translator()

# src - млва оригіналу
# dest мова на яку потрібну перекласти
a = translator.translate('Hello, World!', src='en', dest='uk')

print(a.text)

trans.orgin