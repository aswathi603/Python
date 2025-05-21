"""
OOPs Concepts in Python
1. Class
2. Object
3. Constructor
4. Inheritance
5. Encapsulation
6. Polymorphism
7. Abstraction
8. Method Overriding
9. Method Overloading
10. Operator Overloading
11. Static Method
12. Class Method
13. Instance Method
"""

"""
1. Class: A class is a blueprint for creating objects.
It defines a set of attributes and methods that the created objects will have.

"""

"""
2. Object: An object is an instance of a class.
"""
'''
3. Constructor: A constructor is a special method that is called when an object is created.
'''

'''
4. Inheritance: Inheritance is a way to create a new class that is based on an existing class.
'''

'''
5. Encapsulation: Encapsulation is the bundling of data and methods that operate on that data within one unit, such as a class.
'''

'''
6. Polymorphism: Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface.
'''






'''
class Car :
    color
    model
    Engine
    brand
    interior_color

    now make a class as well as these functions 
    def color(self):
        print("Color of the car is: ", self.color)\
    def model(self):
'''
class Car:
    # Constructor
    def __init__(self, name, color, model, engine, brand, interior_color):
        # Attributes
        self.name = name
        self.color = color
        self.model = model
        self.engine = engine
        self.brand = brand
        self.interior_color = interior_color

    def customerName(self, name):
        self.name = name
        print("Customer Name is: ", self.name)

    def get_Color(self):
        print("Color of the car is: ", self.color)

    def get_Model(self):
        print("Model of the car is: ", self.model)

    def get_Engine(self):
        print("Engine of the car is: ", self.engine)

    def get_Brand(self):
        print("Brand of the car is: ", self.brand)

    def get_Interior_color(self):
        print("Interior color of the car is: ", self.interior_color)


# Creating an object of the Car class
car1 = Car("Aswathi P", "Black", "2025", "V8", "BMW", "Cream")
car1.customerName("Aswathi P")
car1.get_Color()
car1.get_Model()
car1.get_Engine()
car1.get_Brand()
car1.get_Interior_color()

