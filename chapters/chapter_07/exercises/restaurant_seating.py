"""Exercise 07-02: Restaurant Seating

Summary of the book task:
Ask for a dinner group size, convert it to an integer, and decide if there is a wait.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

party_size = int(input("How many people are in your dinner group? "))
if party_size > 8:
    print("You will need to wait for a table.")
else:
    print("Your table is ready.")
