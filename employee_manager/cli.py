import typer
from operations import load_employees, create_employee, save_employee, list_employees, update_employee, delete_employee


app = typer.Typer(help="The Employee Management CLI Application is a simple command-line interface tool to manage "
                       "employees.")


@app.command(help="Create new employee")
def create(name: str, surname: str, age: int, profession: str) -> None:
    employee = create_employee(name=name, surname=surname, age=age, profession=profession)
    response = save_employee(employee)
    print(response)


@app.command(help="List all existing employees")
def list() -> None:
    employees = load_employees()
    list_employees(employees)


@app.command(help="Update existing employee")
def update(name: str, surname: str, attribute_name: str, attribute_value: str) -> None:
    response = update_employee(surname=surname, name=name, attribute_name=attribute_name, attribute_value=attribute_value)
    print(response)


@app.command(help="Delete existing employee")
def delete(name: str, surname: str) -> None:
    response = delete_employee(surname=surname, name=name)
    print(response)


if __name__ == "__main__":
    app()
