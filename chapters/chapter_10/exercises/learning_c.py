"""Exercise 10-02: Learning C

Summary of the book task:
Read the same file and replace the word Python with another language in the output.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path

path = Path(__file__).with_name("learning_python.txt")
for line in path.read_text().splitlines():
    print(line.replace("Python", "C"))
