"""Modul perhitungan geometri."""

import math
from typing import Any, Dict

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


# Fungsi-fungsi perhitungan luas
def square_area(side: float) -> float:
    """Menghitung luas persegi."""
    return side * side


def circle_area(radius: float) -> float:
    """Menghitung luas lingkaran."""
    return math.pi * radius * radius


def triangle_area(base: float, height: float) -> float:
    """Menghitung luas segitiga."""
    return 0.5 * base * height


# Definisi input untuk setiap shape
SHAPE_INPUTS: Dict[str, Dict[str, Any]] = {
    "persegi": {"params": ["sisi"], "function": square_area},
    "lingkaran": {"params": ["jari_jari"], "function": circle_area},
    "segitiga": {"params": ["alas", "tinggi"], "function": triangle_area},
}


def calculate_area() -> None:
    """Hitung luas bangun datar dengan UI interaktif."""
    console.print(Panel("HITUNG LUAS", style="bold cyan"))

    # Dapatkan pilihan shape yang tersedia
    available_shapes = list(SHAPE_INPUTS.keys())
    shapes_display = ", ".join(available_shapes)

    shape = Prompt.ask(
        f"[yellow]Pilih bangun ({shapes_display})[/yellow]", choices=available_shapes
    )

    # Dapatkan definisi input dan fungsi untuk shape yang dipilih
    shape_def = SHAPE_INPUTS[shape]
    param_values = []

    # Minta input sesuai parameter yang dibutuhkan
    for param in shape_def["params"]:
        value = float(Prompt.ask(f"[yellow]Masukkan {param}[/yellow]"))
        param_values.append(value)

    # Hitung luas menggunakan fungsi yang sesuai
    luas = shape_def["function"](*param_values)

    console.print(f"[bold green]Luas: {luas:.2f}[/bold green]")
