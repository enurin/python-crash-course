"""Exercise 04-13: Buffet

Summary of the book task:
Use a tuple for a buffet menu, then replace the tuple with an updated menu.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

foods = ("rice", "beans", "salad", "soup", "bread")
for food in foods:
    print(food)
foods = ("rice", "beans", "fruit", "soup", "pasta")
print("Updated menu:")
for food in foods:
    print(food)
