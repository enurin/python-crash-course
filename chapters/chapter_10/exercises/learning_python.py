"""Exercise 10-01: Learning Python

Summary of the book task:
Read a text file about learning Python and print its contents line by line.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path

path = Path(__file__).with_name("learning_python.txt")
for line in path.read_text().splitlines():
    print(line)
