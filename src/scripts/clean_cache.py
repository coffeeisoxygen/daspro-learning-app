"""Utilitas untuk membersihkan file cache Python."""

import os
import shutil
from pathlib import Path


def clean_cache():
    """Membersihkan semua __pycache__ dan file .pyc dari proyek."""
    project_root = Path(__file__).parent.parent.parent

    count = 0

    # Hapus direktori __pycache__
    for root, dirs, _ in os.walk(project_root):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                cache_path = os.path.join(root, dir_name)
                print(f"Menghapus: {cache_path}")
                shutil.rmtree(cache_path)
                count += 1

    # Hapus file .pyc
    for root, _, files in os.walk(project_root):
        for file in files:
            if file.endswith(".pyc"):
                pyc_file = os.path.join(root, file)
                print(f"Menghapus: {pyc_file}")
                os.remove(pyc_file)
                count += 1

    print(f"Cache dibersihkan! {count} item dihapus.")


if __name__ == "__main__":
    clean_cache()
