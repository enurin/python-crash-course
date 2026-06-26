"""Exercise 05-07: Favorite Fruit

Summary of the book task:
Check whether several fruits appear in a list of favorite fruits.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

favorite_fruits = ["apples", "bananas", "strawberries"]
for fruit in ["bananas", "pears", "apples", "kiwi", "strawberries"]:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!")
