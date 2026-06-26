"""Exercise 03-11: Intentional Error

Summary of the book task:
Create and then fix an index error so you understand list boundaries.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

numbers = [1, 2, 3]
print(numbers[-1])
# An index like numbers[3] would fail because the last valid index is 2.
