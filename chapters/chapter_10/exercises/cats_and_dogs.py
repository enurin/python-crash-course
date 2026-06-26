"""Exercise 10-08: Cats and Dogs

Summary of the book task:
Read cat and dog name files and handle missing files with an error message.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path

for filename in ["cats.txt", "dogs.txt"]:
    path = Path(__file__).with_name(filename)
    try:
        print(path.read_text())
    except FileNotFoundError:
        print(f"Missing file: {filename}")
