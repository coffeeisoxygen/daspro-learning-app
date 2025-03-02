"""Module untuk perhitungan volume bangun ruang."""

import math
from typing import Any, Callable, Dict, List

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# Type alias untuk memperjelas tipe data
VolumeFunction = Callable[..., float]
VolumeConfig = Dict[str, Any]

# Daftar Satuan yang Didukung
AVAILABLE_UNITS = ["cm", "m", "in", "ft"]


def cube_volume(side: float) -> float:
    """Menghitung volume kubus.

    Args:
        side: Panjang sisi kubus

    Returns:
        Volume kubus
    """
    return side * side * side


def sphere_volume(radius: float) -> float:
    """Menghitung volume bola.

    Args:
        radius: Jari-jari bola

    Returns:
        Volume bola
    """
    return (4 / 3) * math.pi * radius * radius * radius


def cylinder_volume(radius: float, height: float) -> float:
    """Menghitung volume tabung.

    Args:
        radius: Jari-jari alas tabung
        height: Tinggi tabung

    Returns:
        Volume tabung
    """
    return math.pi * radius * radius * height


def cuboid_volume(length: float, width: float, height: float) -> float:
    """Menghitung volume balok.

    Args:
        length: Panjang balok
        width: Lebar balok
        height: Tinggi balok

    Returns:
        Volume balok
    """
    return length * width * height


# Definisi input untuk setiap bangun ruang
VOLUME_INPUTS: Dict[str, VolumeConfig] = {
    "kubus": {
        "params": ["sisi"],
        "function": cube_volume,
        "description": "Bangun ruang dengan semua sisi sama panjang",
    },
    "bola": {
        "params": ["jari_jari"],
        "function": sphere_volume,
        "description": "Bangun ruang berbentuk bulat sempurna",
    },
    "tabung": {
        "params": ["jari_jari", "tinggi"],
        "function": cylinder_volume,
        "description": "Bangun ruang dengan alas berbentuk lingkaran",
    },
    "balok": {
        "params": ["panjang", "lebar", "tinggi"],
        "function": cuboid_volume,
        "description": "Bangun ruang dengan sisi berbentuk persegi panjang",
    },
}


def get_validated_input(prompt_text: str) -> float:
    """Mendapatkan dan memvalidasi input numerik dari pengguna.

    Args:
        prompt_text: Teks prompt yang ditampilkan

    Returns:
        float: Nilai numerik yang valid
    """
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


def calculate_volume() -> None:
    """Fungsi utama untuk menghitung volume bangun ruang."""
    console.print(Panel("HITUNG VOLUME", style="bold cyan"))

    # Memilih satuan
    unit = Prompt.ask(
        f"[yellow]Pilih satuan ({', '.join(AVAILABLE_UNITS)})[/yellow]",
        choices=AVAILABLE_UNITS,
    )
    console.print(f"[green]Satuan yang dipilih: {unit}[/green]")

    # Dapatkan pilihan bangun ruang yang tersedia
    available_shapes = list(VOLUME_INPUTS.keys())
    shapes_display = ", ".join(available_shapes)

    shape = Prompt.ask(
        f"[yellow]Pilih bangun ruang ({shapes_display})[/yellow]",
        choices=available_shapes,
    )

    # Tampilkan deskripsi bangun (fitur tambahan)
    console.print(f"[blue]{VOLUME_INPUTS[shape]['description']}[/blue]")

    # Dapatkan definisi input untuk bangun ruang terpilih
    shape_def = VOLUME_INPUTS[shape]
    params = shape_def["params"]

    # Kumpulkan parameter yang dibutuhkan
    param_values: List[float] = []
    for param in params:
        value = get_validated_input(f"[yellow]Masukkan {param} ({unit})[/yellow]: ")
        param_values.append(value)

    # Hitung volume
    result = shape_def["function"](*param_values)

    # Tampilkan hasil dengan format yang rapi
    result_unit = f"{unit}³"
    console.print(
        f"[bold green]Volume {shape}: {result:.2f} {result_unit}[/bold green]"
    )
