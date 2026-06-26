"""Exercise 06-04: Glossary 2

Summary of the book task:
Expand the glossary and loop through all terms and meanings.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

glossary = {"variable": "a name for a value", "list": "an ordered collection", "dictionary": "key-value pairs", "loop": "repeated work", "string": "text"}
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}.")
