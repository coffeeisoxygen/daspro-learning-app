"""Aplikasi CLI utama menampilkan dan mengelola menu interaktif."""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from .calculator import calculator
from .data_types import show_data_types
from .geometry import calculate_area

console = Console()

# Dictionary menu untuk memudahkan penambahan fitur baru
MENU_OPTIONS = {
    "1": {"name": "Pengenalan Tipe Data", "function": show_data_types},
    "2": {"name": "Kalkulator", "function": calculator},
    "3": {"name": "Hitung Luas", "function": calculate_area},
    "0": {"name": "Keluar", "function": None},
}


def display_menu() -> None:
    """Menampilkan menu utama aplikasi."""
    console.print(Panel("=== APLIKASI CLI ===\nPilih fitur:", style="bold blue"))

    for key, option in MENU_OPTIONS.items():
        console.print(f"[{key}] {option['name']}")


def main() -> None:
    """Fungsi utama aplikasi."""
    while True:
        display_menu()

        valid_choices = list(MENU_OPTIONS.keys())
        choice = Prompt.ask(
            "[bold cyan]Masukkan pilihan[/bold cyan]", choices=valid_choices
        )

        if choice == "0":
            console.print("[bold red]Keluar dari program...[/bold red]")
            break

        # Jalankan fungsi yang sesuai dengan pilihan
        selected_function = MENU_OPTIONS[choice]["function"]
        result = selected_function()

        # Jika fungsi mengembalikan nilai, tampilkan
        if result is not None:
            console.print(result)

        input("\nTekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()
