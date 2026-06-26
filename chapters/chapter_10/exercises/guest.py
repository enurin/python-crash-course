"""Exercise 10-04: Guest

Summary of the book task:
Ask for a guest name and write it to a file.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path

name = input("What is your name? ")
path = Path(__file__).with_name("guest.txt")
path.write_text(name + "\n")
print(f"Saved guest name to {path.name}.")
