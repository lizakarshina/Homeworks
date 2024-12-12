# створити клас калькулятор. додати функціію для підрахування суми різниці ділення та множення.

class Calc():
    
    diyi = ['+', '-', '/', '*']
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.diya = diya
        
    def calc(self, diya):
        
        self.diya = diya
        
        if self.diya not in self.diyi:
            return f'Ви ввели неправильну дію\nДоступні дії: {self.diyi}'
        else:
            if self.diya == '+':
                return self.a + self.b
            elif self.diya == '-':
                return self.a - self.b
            elif self.diya == '/':
                return self.a / self.b
            elif self.diya == '*':
                return self.a * self.b


a = int(input('Введіть число 1: '))
b = int(input('Введіть число 2: '))
diya = input('Введіть дію: ')


new_calc = Calc(a, b)
print(new_calc.calc(diya))
print()