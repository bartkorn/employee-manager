class Person:
    
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    def say_hello(self):
        print(f"Hello {self.name} {self.surname} ! You're already {self.age} years old !")
