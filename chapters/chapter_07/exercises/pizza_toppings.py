"""Exercise 07-04: Pizza Toppings

Summary of the book task:
Use a while loop to collect pizza toppings until the user quits.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

prompt = "Enter a pizza topping, or 'quit' to stop: "
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    print(f"Adding {topping}.")
