"""Exercise 06-07: People

Summary of the book task:
Store multiple person dictionaries in a list and print each person details.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

people = [{"first": "ada", "last": "lovelace"}, {"first": "grace", "last": "hopper"}]
for person in people:
    print(f"{person['first'].title()} {person['last'].title()}")
