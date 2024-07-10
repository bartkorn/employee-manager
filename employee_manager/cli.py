import typer
from operations import load_employees, create_employee, save_employee, list_employees, update_employee, delete_employee, load_from_file, get_employee
from validators.validators import validate_property, validate_property_and_value
from presentation.printers import print_table
from processors.processors import convert_to_type
from model.employee import Employee
import os


app = typer.Typer(help="The Employee Management CLI Application is a simple command-line interface tool to manage "
                       "employees.")


@app.command(help="Create new employee")
def create(name: str, surname: str, age: int, profession: str) -> None:
    employee = create_employee(name=name, surname=surname, age=age, profession=profession)
    response = save_employee(employee)
    print(response)


@app.command(help="List all existing employees")
def list(sort: bool = typer.Option(False),  sort_key: str = typer.Option("name")) -> None:
    if sort_key:
        if not validate_property(Employee, sort_key):
            print("Incorrect sort key")
            return None
    employees = load_employees(sort=bool(sort), sort_key=sort_key)
    print_table(Employee, employees)


@app.command(help="List employees and match by property")
def match(match_property: str, match_value: str):
    if not validate_property_and_value(Employee, match_property, match_value):
        print("Incorrect property or value to match")
        return None
    employees = load_employees()
    value = convert_to_type(Employee, match_property, match_value)
    print_table(Employee, employees, True, match_property, value)


@app.command(help="Update existing employee")
def update(name: str, surname: str, attribute_name: str, attribute_value: str) -> None:
    if validate_property_and_value(Employee, attribute_name, attribute_value):
        if get_employee(surname, name) is not None:
            response = update_employee(surname=surname, name=name, attribute_name=attribute_name,
                                       attribute_value=attribute_value)
            print(response)
        else:
            print(f"Employee with given surname '{surname}' and name '{name}' does not exist.")
    else:
        print("Incorrect property name or value.")


@app.command(help="Delete existing employee")
def delete(name: str, surname: str) -> None:
    response = delete_employee(surname=surname, name=name)
    print(response)


@app.command(help="Import employees from file")
def load(filename: str) -> None:
    path = os.path.join(os.getcwd(), filename)
    responses = load_from_file(path)
    print(responses)


if __name__ == "__main__":
    app()
