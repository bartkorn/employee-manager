import unittest
from tests.utils.test_utils import stdout_capture


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.test_person = {
            "name": "Bartlomiej",
            "surname": "Kornowski",
            "age": 36
        }

    def test_say_hello(self):
        from employee_manager.model.person import Person
        person = Person(**self.test_person)
        output = stdout_capture(person.say_hello)

        assert output == f"Hello {self.test_person['name']} {self.test_person['surname']} ! You're already {self.test_person['age']} years old !"