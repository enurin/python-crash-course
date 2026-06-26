"""Exercise 06-01: Person

Summary of the book task:
Store information about one person in a dictionary and print each value.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

person = {"first_name": "ada", "last_name": "lovelace", "age": 36, "city": "london"}
for key, value in person.items():
    print(f"{key}: {value}")
