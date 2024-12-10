# # Створити клас тварина, вписати необхідні атрибути. 
# Створити два об'єкти класу для різних тварин (кіт та собака).

class Animal:
    
    is_tail = True
    who = 'Animal'
    weight = 0
    legs = 4
    is_angry = False
    
    def __init__(self, who, weight):
        self.who = who
        self.weight = weight
        
    def view_info(self):
        print(f'''
    Ким є: {self.who}
    Вага:  {self.weight}
    Дикий: {self.is_angry}
    Хвіст: {self.is_tail}
    Лапи: {self.legs}
              ''')
        
cat = Animal('Cat', '0.2')
cat.view_info()
dog = Animal('Dog', '15')
dog.view_info()        