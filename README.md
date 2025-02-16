![Original Logo](https://github.com/bartkorn/employee-manager/assets/9967734/a6a69dc1-37bb-42cb-bcec-487bd5ad6fbf)
[![Build and Test](https://github.com/bartkorn/employee-manager/actions/workflows/python-app.yml/badge.svg)](https://github.com/bartkorn/employee-manager/actions/workflows/python-app.yml)
## Overview

The Employee Management CLI Application is a simple command-line interface tool designed to manage employees. It provides basic CRUD (Create, Read, Update, Delete) operations to add, edit, and list employees stored in an AWS DynamoDB database. This application is built using Python and leverages Poetry for dependency management and pytest for unit testing.

## Features


* **Add Employee**: Add a new employee to the database.
* **Edit Employee**: Edit existing employee details.
* **List Employees**: List all employees in the database.
* **Delete Employee**: Remove an employee from the database.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

* Python 3.11+
* Poetry
* AWS CLI (configured with appropriate credentials)

## Installation

1. **Clone the repository:**

````
git clone https://github.com/bartkorn/employee-manager.git
cd employee-manager
````
2. **Install dependencies using Poetry:**

````
poetry install
````

3. **Configure AWS credentials:**

Ensure you have AWS CLI installed and configured with your AWS credentials. You can configure it using the following command:
````
aws configure
````

4. **Deploy AWS infrastructure:**

Application uses AWS DynamoDB table to store employee records
```bash
aws cloudformation deploy --template-file employee_manager/iac/dynamodb.yaml --stack-name my-dynamodb-stack
```

## Usage

The application CLI interface allows to perform action on employee data entries. It allows to add new employee, edit existing employee and list all employees.

### Examples
#### Create employee
````
poetry run python employee_manager/cli.py create John Smith 35 construction worker 
````
#### List employees
````
poetry run python employee_manager/cli.py list 
````
#### Update employee
````
poetry run python employee_manager/cli.py update John Smith profession electrician 
````
#### Delete employee
````
poetry run python employee_manager/cli.py delete John Smith
````
#### See help for all available commands 
````
poetry run python employee_manager/cli.py --help 
````

## Running Tests
Unit tests are written using unittest library and pytest for execution. To run the tests, use the following command:

````
poetry run pytest
````
