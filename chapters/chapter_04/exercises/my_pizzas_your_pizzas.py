"""Exercise 04-11: My Pizzas, Your Pizzas

Summary of the book task:
Copy a pizza list, modify each list separately, and print both.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

my_pizzas = ["margherita", "pepperoni", "veggie"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("mushroom")
friend_pizzas.append("hawaiian")
print("My favorite pizzas:")
for pizza in my_pizzas:
    print(pizza)
print("Friend favorite pizzas:")
for pizza in friend_pizzas:
    print(pizza)
