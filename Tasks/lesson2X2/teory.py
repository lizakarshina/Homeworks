# Інкапсуляция це доступ до атрибутів та методів у класі

class MyClass:
    def __init__(self):
        self.public_attribute = "Public attribute"
        self.__private_attribute = "Private attribute"
        self._protected_attribute = "Protected attribute"
    def public_method(self):
        print("This is a public method")
    def __private_method(self):
        print("This is a private method")
    def _protected_method(self):
        print("This is a protected method")
    def how_to_print_private(self):
        print(self.__private_attribute)
        
        
# Наслідування це взяття всії атрибутів і методів у батьківському класі, і можливість їх редагування

class Vehicle: #транспортний засіб
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def drive(self):
        print("The vehicle is in motion.")
    def stop(self):
        print("The vehicle has stopped.")
        
class Car(Vehicle):
    def __init__(self, brand, year, fuel_type):
        # викликаємо конструктор батьківського класу
        super().__init__(brand, year)
        self.fuel_type = fuel_type
    def drive(self):
        print("The car is driving on the road.")
        

# Асоціація це залежцість одного класу від іншого

class Author:
    def __init__(self, name):
        self.name = name
    def write(self):
        print(f"{self.name} is writing a book.")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")
        
        
# Поліморфізм зміна методів батьківського класу під динча

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius