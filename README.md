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

## Usage

The application CLI interface allows to perform action on employee data entries. It allows to add new employee, edit existing employee and list all employees.

To start the CLI application please run:
````
poetry run python employee_manager/main.py
````

## Running Tests
Unit tests are written using unittest library and pytest for execution. To run the tests, use the following command:

````
poetry run pytest
````
