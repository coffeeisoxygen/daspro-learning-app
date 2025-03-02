"""Modul perhitungan geometri."""

import math
from typing import Any, Callable, Dict, List

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# Type alias untuk memperjelas tipe data
ShapeFunction = Callable[..., float]
ShapeConfig = Dict[str, Any]

# Daftar Satuan yang Didukung
AVAILABLE_UNITS = ["cm", "m", "in", "ft"]


def square_area(side: float) -> float:
    """Menghitung luas persegi.

    Args:
        side: Panjang sisi persegi

    Returns:
        Luas persegi
    """
    return side * side


def circle_area(radius: float) -> float:
    """Menghitung luas lingkaran.

    Args:
        radius: Jari-jari lingkaran

    Returns:
        Luas lingkaran
    """
    return math.pi * radius * radius


def triangle_area(base: float, height: float) -> float:
    """Menghitung luas segitiga.

    Args:
        base: Panjang alas segitiga
        height: Tinggi segitiga

    Returns:
        Luas segitiga
    """
    return 0.5 * base * height


# Definisi input untuk setiap bangun
SHAPE_INPUTS: Dict[str, ShapeConfig] = {
    "persegi": {"params": ["sisi"], "function": square_area},
    "lingkaran": {"params": ["jari_jari"], "function": circle_area},
    "segitiga": {"params": ["alas", "tinggi"], "function": triangle_area},
}


def get_validated_input(prompt_text: str) -> float:
    """Mendapatkan dan memvalidasi input numerik dari pengguna."""
    while True:
        try:
            value = float(Prompt.ask(prompt_text))
            if value <= 0:
                console.print(
                    "[bold red]Error: Nilai harus lebih besar dari 0[/bold red]"
                )
                continue
            return value
        except ValueError:
            console.print("[bold red]Error: Masukkan angka yang valid[/bold red]")


def calculate_area() -> None:
    """Fungsi utama untuk menghitung luas bangun geometri."""
    console.print(Panel("HITUNG LUAS", style="bold cyan"))

    # Memilih satuan
    unit = Prompt.ask(
        f"[yellow]Pilih satuan ({', '.join(AVAILABLE_UNITS)})[/yellow]",
        choices=AVAILABLE_UNITS,
    )
    console.print(f"[green]Satuan yang dipilih: {unit}[/green]")

    # Dapatkan pilihan shape yang tersedia
    available_shapes = list(SHAPE_INPUTS.keys())
    shapes_display = ", ".join(available_shapes)

    shape = Prompt.ask(
        f"[yellow]Pilih bangun ({shapes_display})[/yellow]", choices=available_shapes
    )

    # Dapatkan definisi input untuk shape terpilih
    shape_def = SHAPE_INPUTS[shape]
    params = shape_def["params"]

    # Kumpulkan parameter yang dibutuhkan
    param_values: List[float] = []
    for param in params:
        value = get_validated_input(f"Masukkan {param} ({unit}): ")
        param_values.append(value)

    # Hitung luas
    result = shape_def["function"](*param_values)

    # Tampilkan hasil dengan format yang rapi
    result_unit = f"{unit}²"
    console.print(f"[bold green]Luas {shape}: {result:.2f} {result_unit}[/bold green]")
