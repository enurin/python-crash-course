"""Exercise 10-07: Addition Calculator

Summary of the book task:
Wrap the addition calculator in a loop so the user can keep trying.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

while True:
    first = input("First number, or 'quit': ")
    if first == "quit":
        break
    second = input("Second number: ")
    try:
        print(int(first) + int(second))
    except ValueError:
        print("Please enter valid numbers.")
