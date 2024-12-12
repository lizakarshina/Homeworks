# Створити клас Холодильник. Створити атрибути: кількість
# поличок, наявні продукти, скільки років холодильнику.

# Створити функцію, яка буде визначати за допомогою рандому
# чи зламався холодильник. Створити функцію, яка виводитиме
# усі продукти у холодильнику. (Додатково: Створити функцію, 
# яка буде виводити страви, які можна приготувати з наявних
# продуктів у холодильнику (наприклад: ковбаса та хліб = бутерброд))

import random

list_of_products = ['сир', 'ковбаса', 'хліб']

class Fridge:
    
    is_broken = False
    can_cook = []
    
    def __init__(self, polichki, products, age):
        self.polichki = polichki
        self.products = products
        self.age = age
        
    def is_broke(self):
        if self.age > 5:
            num = random.randint(1, 100)
            if num >= 50:
                self.is_broken = True
                return 'Ваш холодильник зламався'
            else:
                return 'Ваш холодильник ne зламався'
        else:
            num = random.randint(1, 100)
            if num >= 70:
                self.is_broken = True
                return 'Ваш холодильник зламався дуже рано :('
            else:
                return 'Ваш холодильник ne зламався'
                
        
    def recipes(self):
        if 'ковбаса' in self.products and 'хліб' in self.products:
            self.can_cook.append('Бутерброд')
        if 'яйце' in self.products:
            self.can_cook.append('Яєшниця')
            
        
        return f'Ти можеш приотувати: {self.can_cook}'
    
    
fridge = Fridge(4, list_of_products, 7)

print(fridge.is_broke())
print(fridge.recipes())