import typer
from operations import load_employees, create_employee, save_employee, list_employees, update_employee


app = typer.Typer()


@app.command()
def create(name: str, surname: str, age: int, profession: str):
    employee = create_employee(name=name, surname=surname, age=age, profession=profession)
    response = save_employee(employee)
    print(response)


@app.command()
def list():
    employees = load_employees()
    list_employees(employees)


@app.command()
def update(name: str, surname: str, attribute_name: str, attribute_value: str ):
    response = update_employee(surname=surname, name=name, attribute_name=attribute_name, attribute_value=attribute_value)
    print(response)


if __name__ == "__main__":
    app()
