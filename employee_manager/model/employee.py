from model.person import Person


class Employee(Person):
    
    def __init__(self, name, surname, age, profession):
        super().__init__(name, surname, age)
        self.profession = profession
        self.hired = False
        
    def get_hired(self):
        self.hired = True
        
    def is_hired(self):
        if self.hired:
            print(f"{self.name} you're hired as {self.profession} !")
        else:
            print(f"{self.name} keep looking for a job !")
        return self.hired
            
    def present(self):
        print(f"Employee {self.name} {self.surname} is working as {self.profession} and is {self.age} years old.")
        
    def to_item(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'profession': self.profession,
            'hired': self.hired
        }