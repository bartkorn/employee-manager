from pydantic import BaseModel


class Person(BaseModel):
    name: str
    surname: str
    age: int
        
    def say_hello(self) -> None:
        print(f"Hello {self.name} {self.surname} ! You're already {self.age} years old !")
