"""Exercise 09-15: Lottery Analysis

Summary of the book task:
Simulate lottery drawings until your ticket wins and count attempts.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from random import choice

choices = [1, 2, 3, 4, 5, "a", "b", "c"]
my_ticket = [1, "a", 3, "c"]
attempts = 0
while True:
    attempts += 1
    ticket = [choice(choices) for _ in range(4)]
    if ticket == my_ticket:
        break
print(f"It took {attempts} tries to win.")
