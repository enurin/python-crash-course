"""Exercise 04-04: One Million

Summary of the book task:
Create a list from 1 to 1,000,000 and inspect it safely.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

numbers = list(range(1, 1_000_001))
# Printing the whole list is noisy; print a small proof instead.
print(numbers[:3])
print(numbers[-3:])
