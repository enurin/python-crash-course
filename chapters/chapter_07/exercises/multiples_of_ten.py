"""Exercise 07-03: Multiples of Ten

Summary of the book task:
Ask for a number and report whether it is a multiple of 10.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

number = int(input("Enter a number: "))
if number % 10 == 0:
    print("That number is a multiple of 10.")
else:
    print("That number is not a multiple of 10.")
