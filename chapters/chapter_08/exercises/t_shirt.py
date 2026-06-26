"""Exercise 08-03: T-Shirt

Summary of the book task:
Write a function with size and message parameters and call it positionally and by keyword.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def make_shirt(size, message):
    """Summarize a shirt order."""
    print(f"Make a {size} shirt that says: {message}")

make_shirt("large", "I love Python")
make_shirt(size="medium", message="Code daily")
