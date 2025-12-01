# common/io.py

import sys
from pathlib import Path

def read_input(default_path: str = "input.txt") -> str:
    """Read from stdin if available, otherwise from the given file path."""

    # fallback: read local file
    file_path = Path(default_path)
    if file_path.exists():
        return file_path.read_text().rstrip("\n")

    raise FileNotFoundError(f"No stdin data and file not found: {default_path}")
