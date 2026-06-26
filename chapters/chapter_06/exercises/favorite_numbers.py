"""Exercise 06-10: Favorite Numbers

Summary of the book task:
Allow each person to have more than one favorite number.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

favorite_numbers = {"ada": [7, 42], "grace": [3, 9], "alan": [11]}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()} likes {numbers}.")
