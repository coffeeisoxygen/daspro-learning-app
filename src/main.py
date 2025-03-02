from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


def show_data_types():
    """Menampilkan pengenalan tipe data dengan tabel."""
    table = Table(
        title="Pengenalan Tipe Data", show_header=True, header_style="bold magenta"
    )
    table.add_column("Tipe", style="cyan", justify="center")
    table.add_column("Contoh", style="green", justify="center")

    table.add_row("Integer", "123")
    table.add_row("Float", "3.14")
    table.add_row("String", "'Hello'")
    table.add_row("Boolean", "True/False")

    console.print(table)


def calculator():
    """Kalkulator sederhana."""
    console.print(Panel("KALKULATOR", style="bold cyan"))

    num1 = float(Prompt.ask("[yellow]Masukkan angka pertama[/yellow]"))
    operator = Prompt.ask(
        "[yellow]Pilih operator (+, -, *, /)[/yellow]", choices=["+", "-", "*", "/"]
    )
    num2 = float(Prompt.ask("[yellow]Masukkan angka kedua[/yellow]"))

    try:
        result = eval(f"{num1} {operator} {num2}")
        console.print(f"[bold green]Hasil: {result}[/bold green]")
    except ZeroDivisionError:
        console.print("[bold red]Error: Pembagian dengan nol![/bold red]")


def calculate_area():
    """Hitung luas bangun datar."""
    console.print(Panel("HITUNG LUAS", style="bold cyan"))

    shape = Prompt.ask(
        "[yellow]Pilih bangun (persegi, lingkaran, segitiga)[/yellow]",
        choices=["persegi", "lingkaran", "segitiga"],
    )

    if shape == "persegi":
        sisi = float(Prompt.ask("[yellow]Masukkan panjang sisi[/yellow]"))
        luas = sisi * sisi

    elif shape == "lingkaran":
        jari_jari = float(Prompt.ask("[yellow]Masukkan jari-jari[/yellow]"))
        luas = 3.14 * jari_jari * jari_jari

    elif shape == "segitiga":
        alas = float(Prompt.ask("[yellow]Masukkan panjang alas[/yellow]"))
        tinggi = float(Prompt.ask("[yellow]Masukkan tinggi[/yellow]"))
        luas = 0.5 * alas * tinggi

    console.print(f"[bold green]Luas: {luas}[/bold green]")


def main():
    while True:
        console.print(Panel("=== APLIKASI CLI ===\nPilih fitur:", style="bold blue"))
        console.print("[1] Pengenalan Tipe Data")
        console.print("[2] Kalkulator")
        console.print("[3] Hitung Luas")
        console.print("[0] Keluar")

        choice = Prompt.ask(
            "[bold cyan]Masukkan pilihan[/bold cyan]", choices=["0", "1", "2", "3"]
        )

        if choice == "1":
            show_data_types()
        elif choice == "2":
            calculator()
        elif choice == "3":
            calculate_area()
        elif choice == "0":
            console.print("[bold red]Keluar dari program...[/bold red]")
            break

        input("\nTekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()
