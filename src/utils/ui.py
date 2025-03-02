"""Utilitas UI yang digunakan di seluruh aplikasi."""

from rich.console import Console
from rich.panel import Panel

console = Console()


def display_title(title: str) -> None:
    """Menampilkan judul dalam panel."""
    console.print(Panel(title, style="bold cyan"))
