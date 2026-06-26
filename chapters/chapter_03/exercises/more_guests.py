"""Exercise 03-06: More Guests

Summary of the book task:
Expand the dinner guest list after finding a bigger table and invite everyone.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

guests = ["ada lovelace", "grace hopper", "alan turing"]
print("I found a bigger dinner table.")
guests.insert(0, "katherine johnson")
guests.insert(2, "margaret hamilton")
guests.append("dorothy vaughan")
for guest in guests:
    print(f"Dear {guest.title()}, please join me for dinner.")
