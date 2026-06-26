"""Exercise 09-14: Lottery

Summary of the book task:
Build a small lottery drawing from numbers and letters.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from random import choice

choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
winning_ticket = [choice(choices) for _ in range(4)]
print("Winning ticket:", winning_ticket)
