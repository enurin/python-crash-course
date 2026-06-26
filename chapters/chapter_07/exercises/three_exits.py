"""Exercise 07-06: Three Exits

Summary of the book task:
Rewrite the topping loop using one of the common loop-exit strategies.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

prompt = "Enter a topping, or 'quit': "
active = True
while active:
    topping = input(prompt)
    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping}.")
