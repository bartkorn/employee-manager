class Person:
    
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        
    def say_hello(self) -> None:
        print(f"Hello {self.name} {self.surname} ! You're already {self.age} years old !")
