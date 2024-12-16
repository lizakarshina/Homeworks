# Написати клас пристрій.
# Він має бути батьківським класом для телефона, планшета та комп'ютера. 
# Написати для батьківського класу метод який виводить "привіт, я пристрій!". 
# створити атрибут назва пристрою та ініціалізувати його для кожного класу. 
# Переробити метод батьківського класу під кожен наслідуваний клас.

class Device:
    def __init__(self, type):
        self.type = type
        pass
    
    def show_type(self):
        print('Привіт, я пристрій')
        
        
class Smartphone(Device):
    name = 'Телефон'
    def __init__(self):
        super().__init__(self.name)
        
    def show_type(self):
        print(f'Привіт, я {self.name}')
        
        
class Tablet(Device):
    name = 'Планшет'
    def __init__(self):
        super().__init__(self.name)
        
    def show_type(self):
        print(f'Привіт, я {self.name}')
        
        
class Computer(Device):
    name = "Комп'ютер"
    def __init__(self):
        super().__init__(self.name)
        
    def show_type(self):
        print(f'Привіт, я {self.name}')
        
        
        
phone = Smartphone()
pc = Computer()
tablet = Tablet()


phone.show_type()
pc.show_type()
tablet.show_type()