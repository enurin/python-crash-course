"""Exercise 06-06: Polling

Summary of the book task:
Compare a list of people with poll responses and invite missing people to respond.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust"}
people = ["jen", "sarah", "phil", "erin"]
for person in people:
    if person in favorite_languages:
        print(f"Thanks, {person.title()}, for responding.")
    else:
        print(f"{person.title()}, please take the poll.")
