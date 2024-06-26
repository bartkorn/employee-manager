from model.employee import Employee
from client.database import get_all_items, save_item, update_item, delete_item
from typing import List


def load_employees() -> List[Employee]:
    return [Employee(**item) for item in get_all_items('Employees')]


def list_employees(employees: List[Employee]) -> None:
    for employee in employees:
        employee.present()


def create_employee(name: str, surname: str, age: int, profession: str) -> Employee:
    return Employee(name=name, surname=surname, age=age, profession=profession)


def save_employee(employee: Employee) -> str:
    response = save_item('Employees', employee.to_item())
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return 'Employee created successfully'
    else:
        return 'Error during adding employee'


def update_employee(surname: str, name: str, attribute_name: str, attribute_value: any) -> str:
    response = update_item('Employees', 'surname', surname, 'name', name, attribute_name, attribute_value)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return 'Employee updated successfully'
    else:
        return 'Error during employee update'


def delete_employee(surname: str, name: str) -> str:
    response = delete_item('Employees', 'surname', surname, 'name', name)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return 'Employee deleted successfully'
    else:
        return 'Error during employee delete'

