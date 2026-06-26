"""Exercise 06-08: Pets

Summary of the book task:
Store pet dictionaries in a list and print information about each pet.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

pets = [{"animal": "dog", "owner": "ada"}, {"animal": "cat", "owner": "grace"}]
for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']}.")
