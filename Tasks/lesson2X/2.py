# Створити клас кіт. Вказати необхідні атрибути для класу кіт.
# Створити об'єкти класу для різних порід та видів котів.

class Cat:
    name = ''
    poroda = 'Dikiy'
    waga = 0
    age = 0
    stat = ''
    is_silly = True
    can_hunt = False
    is_pet = True
    
    def __init__ (self, name, waga, age, stat, poroda='Dikiy'):
        self.name = name
        self.poroda = poroda
        self.waga = waga
        self.age = age
        self.stat = stat

    def view_info(self):
        print(f'''
    Ким є: {self.name}
    Вага:  {self.waga}
    Poroda: {self.poroda}
    age: {self.age}
    stat: {self.stat}
              ''')
        
        
cat1 = Cat('Tsar', waga=5, age=7, stat='Man')
cat = Cat('Max', 6, 6, 'Man', 'British')

cat1.view_info()
cat.view_info()
