"""Exercise 07-08: Deli

Summary of the book task:
Move sandwich orders from one list to another as each sandwich is made.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

sandwich_orders = ["tuna", "pastrami", "veggie", "turkey"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
