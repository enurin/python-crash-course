"""Exercise 04-09: Cube Comprehension

Summary of the book task:
Build the first ten cubes with a list comprehension.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

cubes = [number**3 for number in range(1, 11)]
print(cubes)
