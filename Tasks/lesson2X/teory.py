class OsviTech (object):
    attr1 = 42
    attr2 = 'Hello, world'
    

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def method(self, something):
        return f'{self.name}, {self.age}'
        
student1 = Student('Пук', 20)
student1 = Student('Пук2', 22)


type() # визначає тип об'єкту

class MyClass:
    def __init__(self):
        pass
    # ???
    @staticmethod
    def static_method ():
        pass
    
    @classmethod
    def classmethod ():
        pass

# ???
class MyClass2:
    def __new__(cls):
        
        instance = super().__new__(cls)  
        pass
    
    

    def __del__ (self):
        print("Виведеться коли об'єкт видалиться")