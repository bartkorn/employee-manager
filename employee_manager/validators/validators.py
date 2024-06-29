from typing import get_type_hints


def validate_is_bool(value: str) -> bool:
    return value.lower() in ['true', 'false']


def validate_is_other(expected_type, value: any) -> bool:
    try:
        expected_type(value)
        return True
    except ValueError:
        return False


def validate_property(cls, attr_name: any, attr_value: any) -> bool:
    if attr_name in get_type_hints(cls):
        if get_type_hints(cls).get(attr_name) == bool:
            return validate_is_bool(attr_value)
        else:
            return validate_is_other(get_type_hints(cls).get(attr_name), attr_value)
    return False
