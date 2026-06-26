"""Exercise 06-03: Glossary

Summary of the book task:
Build a small programming glossary with dictionary key-value pairs.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

glossary = {"variable": "a name for a value", "list": "an ordered collection", "dictionary": "key-value pairs"}
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}.")
