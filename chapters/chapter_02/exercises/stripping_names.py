"""Exercise 02-07: Stripping Names

Summary of the book task:
Store a name with extra whitespace and show how strip methods clean it up.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

name = "\tAda Lovelace\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
