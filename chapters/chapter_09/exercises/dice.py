"""Exercise 09-13: Dice

Summary of the book task:
Create a Die class and roll dice with different numbers of sides.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

for sides in (6, 10, 20):
    die = Die(sides)
    print(f"Rolling a D{sides}:", [die.roll_die() for _ in range(10)])
