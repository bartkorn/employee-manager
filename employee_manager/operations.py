import boto3.exceptions

from model.employee import Employee
from client.database import get_all_items, save_item, update_item, delete_item, get_item, batch_save
from typing import List
from processors.io import read_csv, read_header


def load_employees(sort: bool = False, sort_key: str = "") -> List[Employee]:
    employees = [Employee(**item) for item in get_all_items('Employees')]
    if sort:
        return sorted(employees, key=lambda employee: employee.to_item()[sort_key])
    return employees


def get_employee(surname: str, name: str) -> Employee | None:
    response = get_item('Employees', 'surname', surname, 'name', name)
    if 'Item' in response:
        return Employee(**response['Item'])
    return None


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


def load_from_file(path: str) -> str:
    loaded_cnt: int = 0
    header: list | bool = read_header(path, Employee)
    if not header:
        print("Header is broken")
    items = read_csv(path, header, Employee)
    if not items:
        print("CSV failed to load")
    try:
        batch_save(table_name='Employees', items=items)
        return f"{len(items)} employees successfully loaded."
    except boto3.exceptions.Boto3Error:
        return "Error while loading employees."
