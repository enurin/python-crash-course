"""Exercise 10-12: Favorite Number Remembered

Summary of the book task:
Load a remembered favorite number when it exists, otherwise ask and save it.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path
import json


path = Path(__file__).with_name("favorite_number.json")
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}.")
