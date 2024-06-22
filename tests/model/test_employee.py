import unittest
from tests.utils.test_utils import stdout_capture


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.test_employee = {
            "name": "Bartlomiej",
            "surname": "Kornowski",
            "age": 36,
            "profession": "Manager"
        }

    def test_get_hired(self):
        from employee_manager.model.employee import Employee
        employee = Employee(**self.test_employee)
        assert employee.is_hired() == False
        employee.get_hired()
        assert employee.is_hired() == True

    def test_present(self):
        from employee_manager.model.employee import Employee
        employee = Employee(**self.test_employee)
        output = stdout_capture(employee.present)
        assert output == f"Employee {self.test_employee['name']} {self.test_employee['surname']} is working as {self.test_employee['profession']} and is {self.test_employee['age']} years old."

    def test_to_item(self):
        from employee_manager.model.employee import Employee
        employee = Employee(**self.test_employee)
        item = employee.to_item()
        assert item["name"] == self.test_employee["name"]
        assert item["surname"] == self.test_employee["surname"]
        assert item["profession"] == self.test_employee["profession"]
        assert item["age"] == self.test_employee["age"]


