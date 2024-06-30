from rich.console import Console
from rich.table import Table
from typing import get_type_hints, Dict


def print_table(model: any, iterable: any, highlight: bool = False, property_name: str = "", match_value: any = None) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold blue")
    for key in get_type_hints(model).keys():
        table.add_column(key.capitalize(), style="bold")
    for item in iterable:
        if highlight:
            table.add_row(*[highlight_record(item.to_item(), prop, property_name, match_value) for prop in get_type_hints(model)])
        else:
            table.add_row(*[str(item.to_item()[prop]) for prop in get_type_hints(model)])
    console.print(table)


def highlight_record(item: Dict, property_name: str, match_property: str,  match_value: any) -> str:
    if property_name == match_property and item.get(property_name) == match_value:
        return f"[yellow]{item.get(property_name)}[/]"
    return f"{item.get(property_name)}"
