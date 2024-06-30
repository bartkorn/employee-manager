from typing import get_type_hints


def convert_to_type(cls, property_name: str, property_value: str) -> any:
    if get_type_hints(cls).get(property_name) == bool:
        match property_value.lower():
            case "true":
                return True
            case "false":
                return False
            case other:
                return False
    return get_type_hints(cls).get(property_name)(property_value)