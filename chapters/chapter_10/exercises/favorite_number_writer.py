"""Exercise 10-11: Favorite Number

Summary of the book task:
Ask for a favorite number and store it in JSON.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path
import json

number = input("What is your favorite number? ")

path = Path(__file__).with_name("favorite_number.json")
contents = json.dumps(number)
path.write_text(contents)

print("Thanks! I'll remember your favorite number.")
