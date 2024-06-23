from model.employee import Employee
from client.database import get_all_items, save_item, update_item


def load_employees():
    return [Employee(
        item['name'],
        item['surname'],
        int(item['age']),
        item['profession']) for item in get_all_items('Employees')]


def list_employees(employees):
    for employee in employees:
        employee.present()


def create_employee(name, surname, age, profession):
    return Employee(name=name, surname=surname, age=age, profession=profession)


def save_employee(employee):
    response = save_item('Employees', employee.to_item())
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return 'Employee created successfully'
    else:
        return 'Error during adding employee'


def update_employee(surname, name, attribute_name, attribute_value):
    response = update_item('Employees', 'surname', surname, 'name', name, attribute_name, attribute_value)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return 'Employee updated successfully'
    else:
        return 'Error during employee update'

