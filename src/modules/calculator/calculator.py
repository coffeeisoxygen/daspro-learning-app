"""Modul kalkulator sederhana."""

import math
from typing import Callable, Dict, Union

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

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


def calculator() -> None:
    """Kalkulator sederhana dengan UI interaktif."""
    console.print(Panel("KALKULATOR", style="bold cyan"))

    valid_operators = list(OPERATIONS.keys())
    operator_display = ", ".join(valid_operators)

    num1 = float(Prompt.ask("[yellow]Masukkan angka pertama[/yellow]"))
    operator = Prompt.ask(
        f"[yellow]Pilih operator ({operator_display})[/yellow]", choices=valid_operators
    )
    num2 = float(Prompt.ask("[yellow]Masukkan angka kedua[/yellow]"))

    try:
        result = perform_operation(num1, operator, num2)
        console.print(f"[bold green]Hasil: {result}[/bold green]")
    except ZeroDivisionError:
        console.print("[bold red]Error: Pembagian dengan nol![/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        console.print("[bold red]Silakan coba lagi.[/bold red]")
