"""Exercise 04-08: Cubes

Summary of the book task:
Build a list of the first ten cubes with a loop.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

cubes = []
for number in range(1, 11):
    cubes.append(number**3)
print(cubes)
