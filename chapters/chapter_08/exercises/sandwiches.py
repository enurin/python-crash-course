"""Exercise 08-12: Sandwiches

Summary of the book task:
Use arbitrary positional arguments to collect sandwich ingredients.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def make_sandwich(*items):
    print("Making a sandwich with:")
    for item in items:
        print(f"- {item}")

make_sandwich("turkey", "lettuce")
make_sandwich("tuna")
make_sandwich("hummus", "tomato", "cucumber")
