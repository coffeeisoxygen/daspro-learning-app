"""Modul kalkulator sederhana."""

import math
from typing import Callable, Dict, Optional, Union

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# Dictionary untuk memetakan operator ke fungsi
OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else float("nan"),
    "^": lambda x, y: math.pow(x, y),
    "%": lambda x, y: x % y if y != 0 else float("nan"),
}


def perform_operation(num1: float, operator: str, num2: float) -> Union[float, str]:
    """Melakukan operasi matematika.

    Args:
        num1: Angka pertama
        operator: Operator matematika
        num2: Angka kedua

    Returns:
        Hasil perhitungan atau pesan error
    """
    if operator not in OPERATIONS:
        return "Operator tidak valid"

    result = OPERATIONS[operator](num1, num2)

    if math.isnan(result):
        raise ZeroDivisionError("Pembagian dengan nol!")

    return result


def validate_input(
    prompt: str,
    type_: type = float,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
) -> Union[float, str]:
    """Memvalidasi input pengguna.

    Args:
        prompt: Pesan yang ditampilkan ke pengguna
        type_: Tipe data yang diharapkan
        min_value: Nilai minimum (opsional)
        max_value: Nilai maksimum (opsional)

    Returns:
        Input yang valid sesuai tipe data yang diminta
    """
    while True:
        try:
            value = type_(Prompt.ask(prompt))

            # Validasi batas minimum jika ada
            if min_value is not None and value < min_value:
                console.print(
                    f"[bold red]Error: Nilai harus lebih besar atau sama dengan {min_value}[/bold red]"
                )
                continue

            # Validasi batas maksimum jika ada
            if max_value is not None and value > max_value:
                console.print(
                    f"[bold red]Error: Nilai harus lebih kecil atau sama dengan {max_value}[/bold red]"
                )
                continue

            return value
        except ValueError:
            console.print(
                "[bold red]Error: Input tidak valid. Harap masukkan angka yang valid.[/bold red]"
            )


def display_operator_help() -> None:
    """Menampilkan bantuan tentang operator yang tersedia."""
    table = Table(title="Operator yang tersedia", show_header=True)
    table.add_column("Operator", style="cyan")
    table.add_column("Deskripsi", style="green")
    table.add_column("Contoh", style="yellow")

    table.add_row("+", "Penjumlahan", "5 + 3 = 8")
    table.add_row("-", "Pengurangan", "5 - 3 = 2")
    table.add_row("*", "Perkalian", "5 * 3 = 15")
    table.add_row("/", "Pembagian", "6 / 2 = 3")
    table.add_row("^", "Pangkat", "2 ^ 3 = 8")
    table.add_row("%", "Modulus (sisa bagi)", "7 % 3 = 1")

    console.print(table)


def calculator() -> None:
    """Kalkulator sederhana dengan UI interaktif."""
    console.print(Panel("KALKULATOR", style="bold cyan"))

    # Tawarkan bantuan untuk pengguna
    help_option = Prompt.ask(
        "[yellow]Lihat bantuan operator? (y/n)[/yellow]",
        choices=["y", "n"],
        default="n",
    )

    if help_option.lower() == "y":
        display_operator_help()

    # Gunakan fungsi validasi yang ada untuk input
    num1 = validate_input("[yellow]Masukkan angka pertama[/yellow]")

    # Tampilkan pilihan operator
    valid_operators = list(OPERATIONS.keys())
    operator_display = ", ".join(valid_operators)
    operator = Prompt.ask(
        f"[yellow]Pilih operator ({operator_display})[/yellow]", choices=valid_operators
    )

    # Validasi input kedua dengan konteks operator
    # Jika pembagian atau modulus, hindari nol
    if operator in ["/", "%"]:
        num2 = validate_input(
            "[yellow]Masukkan angka kedua[/yellow]",
            min_value=0.000001,  # Nilai minimum kecil untuk menghindari nol
        )
    else:
        num2 = validate_input("[yellow]Masukkan angka kedua[/yellow]")

    try:
        result = perform_operation(num1, operator, num2)
        console.print(f"[bold green]Hasil: {result}[/bold green]")

        # Tampilkan ekspresi matematika yang dihitung
        console.print(f"[blue]{num1} {operator} {num2} = {result}[/blue]")
    except ZeroDivisionError:
        console.print("[bold red]Error: Pembagian dengan nol![/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        console.print("[bold red]Silakan coba lagi.[/bold red]")


if __name__ == "__main__":
    calculator()
