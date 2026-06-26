"""Exercise 07-09: No Pastrami

Summary of the book task:
Remove all pastrami orders from a sandwich list before making the remaining orders.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

sandwich_orders = ["pastrami", "tuna", "pastrami", "veggie", "pastrami"]
print("The deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)
