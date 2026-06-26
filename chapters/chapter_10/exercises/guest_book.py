"""Exercise 10-05: Guest Book

Summary of the book task:
Collect multiple guest names in a loop and write them to a guest book file.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path

path = Path(__file__).with_name("guest_book.txt")
path.write_text("")

while True:
    name = input("Enter your name, or 'quit': ")
    if name == "quit":
        break

    print(f"Welcome, {name.title()}!")
    with path.open("a") as file:
        file.write(name + "\n")

print(f"Saved guest names to {path.name}.")
