"""Exercise 08-04: Large Shirts

Summary of the book task:
Add default values to the shirt function and override them when needed.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def make_shirt(size="large", message="I love Python"):
    """Summarize a shirt order with defaults."""
    print(f"Make a {size} shirt that says: {message}")

make_shirt()
make_shirt("medium")
make_shirt("small", "Keep learning")
