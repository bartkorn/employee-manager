import boto3
import unittest
import io
import sys
from moto import mock_aws
from tests.utils.test_utils import stdout_capture


class TestOperations(unittest.TestCase):

    def setUp(self):
        self.mock_aws = mock_aws()
        self.mock_aws.start()
        dynamodb = boto3.resource('dynamodb')
        dynamodb.create_table(
            TableName='Employees',
            KeySchema=[
                {
                    'AttributeName': 'surname',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'surname',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table = dynamodb.Table('Employees')
        table.put_item(Item={
            'surname': 'Kornowski',
            'name': 'Bartlomiej',
            'age': 36,
            'profession': 'Manager'
        })

    def test_list_employees(self):
        from operations import list_employees
        from model.employee import Employee
        employees = [Employee(
            name='Bartlomiej',
            surname='Kornowski',
            age=36,
            profession='Manager'
        )]

        output = stdout_capture(list_employees, employees)
        assert output == f"Employee Bartlomiej Kornowski is working as Manager and is 36 years old."

    def test_create_employee(self):
        from operations import create_employee
        employee = create_employee(
            name="Bartlomiej",
            surname="Kornowski",
            age=35,
            profession="Manger"
        )
        assert employee.name == 'Bartlomiej'

    @mock_aws
    def test_save_employee(self):
        from operations import save_employee
        from model.employee import Employee

        response = save_employee(Employee(
            name='Bartlomiej',
            surname='Kornowski',
            age=36,
            profession='Manager'
        ))
        assert response == 'Employee created successfully'

    @mock_aws
    def test_load_employees(self):
        from operations import load_employees
        employees = load_employees()
        assert len(employees) == 1
        assert employees[0].surname == 'Kornowski'
        assert employees[0].name == 'Bartlomiej'
        assert employees[0].age == 36
        assert employees[0].profession == 'Manager'

    @mock_aws
    def test_update_employee(self):
        from operations import update_employee

        response = update_employee(
            surname='Kornowski',
            name='Bartlomiej',
            attribute_name='age',
            attribute_value=30
        )
        assert response == "Employee updated successfully"

    @mock_aws
    def test_delete_employee(self):
        from operations import delete_employee

        response = delete_employee(surname='Kornowski', name='Bartlomiej')
        assert response == "Employee deleted successfully"

    def tearDown(self):
        self.mock_aws.stop()


if __name__ == "__main__":
    unittest.main()
