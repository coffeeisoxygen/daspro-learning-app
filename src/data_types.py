"""Module for handling data type demonstrations in Python."""

from typing import List, Tuple

from rich.console import Console
from rich.table import Table

console = Console()

DataTypeEntry = Tuple[str, str, str, str, str, str]


def get_data_types() -> List[DataTypeEntry]:
    """Return the list of data type information.

    Returns:
        List[DataTypeEntry]: List of tuples containing data type information
    """
    return [
        (
            "Teks",
            "String",
            "Teks atau karakter",
            "'Hello'",
            "type('Hello') → str",
            "'A' + 'B' → 'AB'",
        ),
        ("Angka", "Integer", "Angka bulat", "123", "type(123) → int", "10 + 5 → 15"),
        (
            "Angka",
            "Float",
            "Angka desimal",
            "3.14",
            "type(3.14) → float",
            "2.5 * 2 → 5.0",
        ),
        (
            "Sequence",
            "List",
            "Kumpulan elemen yang bisa diubah",
            "[1,2,3]",
            "type([1,2,3]) → list",
            "[1,2,3].append(4)",
        ),
        (
            "Sequence",
            "Tuple",
            "Kumpulan elemen yang tidak bisa diubah",
            "(1,2,3)",
            "type((1,2,3)) → tuple",
            "(1,2) + (3,4) → (1,2,3,4)",
        ),
        (
            "Mapping",
            "Dictionary",
            "Key-value pair",
            "{'a':1}",
            "type({'a':1}) → dict",
            "dict['a'] → 1",
        ),
        (
            "Set",
            "Set",
            "Kumpulan unik, tidak berurut",
            "{1,2,3}",
            "type({1,2,3}) → set",
            "{1,2,3} | {3,4,5} → {1,2,3,4,5}",
        ),
        (
            "Boolean",
            "Boolean",
            "Nilai benar atau salah",
            "True / False",
            "type(True) → bool",
            "2 > 1 → True",
        ),
        (
            "Binary",
            "Bytes",
            "Data biner",
            "b'hello'",
            "type(b'hello') → bytes",
            "b'abc' + b'de' → b'abcde'",
        ),
        (
            "None",
            "NoneType",
            "Nilai kosong",
            "None",
            "type(None) → NoneType",
            "None == None → True",
        ),
    ]


def show_data_types() -> Table:
    """Create and return a formatted table showing Python data types.

    Returns:
        Table: A Rich table object containing data type information
    """
    table = Table(title="Pengenalan Tipe Data di Python", header_style="bold magenta")

    # Add columns
    table.add_column("Tipe Utama", style="cyan", justify="center")
    table.add_column("Jenis", style="blue", justify="center")
    table.add_column("Penjelasan", style="yellow", justify="left")
    table.add_column("Contoh Nilai", style="green", justify="center")
    table.add_column("Contoh Kode", style="red", justify="left")
    table.add_column("Contoh Operasi", style="bold", justify="left")

    # Add rows from data
    for entry in get_data_types():
        table.add_row(*entry)

    return table
