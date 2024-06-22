from operations import load_employees, create_employee, save_employee, list_employees, update_employee


def main():
    employees = load_employees()

    while True:

        option = int(input("Select option: \n\t1/ Add employee \n\t2/ List employees \n\t3/ Update employee \n\t4/ Exit \nSelection: "))

        match option:
            case 1:
                employee = create_employee()
                response = save_employee(employee)
                print(response)
                continue
            case 2:
                employees = load_employees()
                list_employees(employees)
                continue
            case 3:
                surname = input("Enter employee surname: ")
                name = input("Enter employee name: ")
                attribute_name = input("Enter property to update [age / profession]: ")
                attribute_value = input("Enter value of property to update: ")
                response = update_employee(surname, name, attribute_name, attribute_value)
                print(response)
                continue
            case 4:
                break
            case other:
                print("Invalid option")
                continue


if __name__ == "__main__":
    main()
