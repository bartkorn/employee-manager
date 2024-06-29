from rich.console import Console
from rich.table import Table
from typing import get_type_hints


def print_table(model: any, iterable: any) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold blue")
    for key in get_type_hints(model).keys():
        table.add_column(key.capitalize(), style="bold")
    for item in iterable:
        table.add_row(*[str(item.to_item()[prop]) for prop in get_type_hints(model)])
    console.print(table)
