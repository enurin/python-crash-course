"""Exercise 06-09: Favorite Places

Summary of the book task:
Store each person favorite places as lists inside a dictionary.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

favorite_places = {"ada": ["london", "paris"], "grace": ["new york"], "alan": ["manchester", "cambridge"]}
for name, places in favorite_places.items():
    print(f"{name.title()} likes:")
    for place in places:
        print(f"- {place.title()}")
