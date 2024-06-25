from model.person import Person
from typing import Dict


class Employee(Person):
    profession: str
    hired: bool = False

    def get_hired(self) -> None:
        self.hired = True
        
    def is_hired(self) -> bool:
        if self.hired:
            print(f"{self.name} you're hired as {self.profession} !")
        else:
            print(f"{self.name} keep looking for a job !")
        return self.hired
            
    def present(self) -> None:
        print(f"Employee {self.name} {self.surname} is working as {self.profession} and is {self.age} years old.")
        
    def to_item(self) -> Dict:
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'profession': self.profession,
            'hired': self.hired
        }