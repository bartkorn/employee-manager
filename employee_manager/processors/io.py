import csv
from typing import Dict, get_type_hints
from validators.validators import validate_property, validate_property_and_value


def validate_header(file_name: str) -> bool:
    pass


def read_header(file_name: str, cls: any) -> list | bool:

    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)

    for head in header:
        if head not in get_type_hints(cls).keys():
            return False
    return header


def read_csv(file_name: str, header: list, cls: any) -> list | bool:

    rows: list[cls] = []

    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            row_item = {}
            for idx in range(len(header)):
                if not validate_property_and_value(cls, header[idx], row[idx]):
                    return False
                row_item[header[idx]] = row[idx]
            rows.append(cls(**row_item).to_item())

    return rows


