"""Exercise 10-06: Addition

Summary of the book task:
Add two numbers and catch ValueError when the user types non-numeric input.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

try:
    first = int(input("First number: "))
    second = int(input("Second number: "))
except ValueError:
    print("Please enter numbers only.")
else:
    print(first + second)
