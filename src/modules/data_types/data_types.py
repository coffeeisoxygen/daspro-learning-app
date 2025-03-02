"""Module for handling data type demonstrations in Python."""

from typing import Dict, List, Tuple

from rich.console import Console
from rich.table import Table

console = Console()

DataTypeEntry = Tuple[str, str, str, str, str]


def get_data_types() -> List[DataTypeEntry]:
    """Return the list of data type information.

    Returns:
        List[DataTypeEntry]: List of tuples containing data type information
    """
    return [
        # Text Type
        (
            "Text",
            "str",
            "Teks atau rangkaian karakter",
            "'Hello World'",
            "text = 'Python'",
        ),
        # Numeric Types
        (
            "Numeric",
            "int",
            "Bilangan bulat tanpa desimal",
            "42, -7, 0",
            "count = 100",
        ),
        (
            "Numeric",
            "float",
            "Bilangan desimal",
            "3.14, -0.001, 2e3",
            "pi = 3.14159",
        ),
        (
            "Numeric",
            "complex",
            "Bilangan kompleks dengan bagian real dan imajiner",
            "1+2j, 3-4j",
            "c = 2+3j",
        ),
        # Sequence Types
        (
            "Sequence",
            "list",
            "Koleksi berurutan yang dapat diubah",
            "[1, 2, 3], ['a', 'b']",
            "numbers = [1, 2, 3]",
        ),
        (
            "Sequence",
            "tuple",
            "Koleksi berurutan yang tidak dapat diubah",
            "(1, 2, 3), ('a', 'b')",
            "point = (10, 20)",
        ),
        (
            "Sequence",
            "range",
            "Urutan angka yang tidak dapat diubah",
            "range(5) → 0,1,2,3,4",
            "r = range(1, 10, 2)",
        ),
        # Mapping Type
        (
            "Mapping",
            "dict",
            "Koleksi pasangan key-value yang dapat diubah",
            "{'name': 'John', 'age': 30}",
            "person = {'id': 101, 'name': 'Alice'}",
        ),
        # Set Types
        (
            "Set",
            "set",
            "Koleksi tidak berurutan tanpa duplikat yang dapat diubah",
            "{1, 2, 3}, set([1, 2, 3])",
            "unique_nums = {1, 2, 3, 3}",
        ),
        (
            "Set",
            "frozenset",
            "Koleksi tidak berurutan tanpa duplikat yang tidak dapat diubah",
            "frozenset({1, 2, 3})",
            "fs = frozenset(['a', 'b', 'c'])",
        ),
        # Boolean Type
        (
            "Boolean",
            "bool",
            "Nilai logika benar atau salah",
            "True, False",
            "is_valid = True",
        ),
        # Binary Types
        (
            "Binary",
            "bytes",
            "Urutan byte yang tidak dapat diubah",
            "b'hello'",
            "data = b'\\x00\\x01'",
        ),
        (
            "Binary",
            "bytearray",
            "Urutan byte yang dapat diubah",
            "bytearray(b'hello')",
            "ba = bytearray(5)",
        ),
        (
            "Binary",
            "memoryview",
            "Tampilan memori objek biner",
            "memoryview(b'abc')",
            "mv = memoryview(bytes(5))",
        ),
        # None Type
        (
            "None",
            "NoneType",
            "Mewakili nilai kosong atau tidak ada",
            "None",
            "result = None",
        ),
    ]


def show_data_types() -> Table:
    """Create and return a formatted table showing Python data types.

    Returns:
        Table: A Rich table object containing data type information
    """
    table = Table(title="Pengenalan Tipe Data di Python", header_style="bold magenta")

    # Add columns
    table.add_column("Kategori", style="cyan", justify="center")
    table.add_column("Tipe", style="blue", justify="center")
    table.add_column("Penjelasan", style="yellow", justify="left")
    table.add_column("Contoh", style="green", justify="center")
    table.add_column("Contoh Assignment", style="red", justify="left")

    # Add rows from data
    for entry in get_data_types():
        table.add_row(*entry)

    return table


def get_data_types_by_category() -> Dict[str, List[DataTypeEntry]]:
    """Return data types grouped by categories.

    Returns:
        Dict[str, List[DataTypeEntry]]: Dictionary with categories as keys and lists of data types as values
    """
    data_types = get_data_types()
    categories = {}

    for data_type in data_types:
        category = data_type[0]
        if category not in categories:
            categories[category] = []
        categories[category].append(data_type)

    return categories
