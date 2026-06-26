"""Exercise 10-03: Simpler Code

Summary of the book task:
Use a simpler file-reading approach than the first version.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path

path = Path(__file__).with_name("learning_python.txt")
contents = path.read_text()
print(contents)
