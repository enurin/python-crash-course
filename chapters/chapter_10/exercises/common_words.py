"""Exercise 10-10: Common Words

Summary of the book task:
Count occurrences of a common word in a sample text file.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path

path = Path(__file__).with_name("sample_book.txt")
text = path.read_text().lower()
print(text.count("the"))
print(text.count("the "))
