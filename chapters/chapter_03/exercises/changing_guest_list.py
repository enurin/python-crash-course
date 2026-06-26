"""Exercise 03-05: Changing Guest List

Summary of the book task:
Replace a guest who cannot attend and print a new set of invitations.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

guests = ["ada lovelace", "grace hopper", "alan turing"]
print(f"{guests[1].title()} cannot make it.")
guests[1] = "katherine johnson"
for guest in guests:
    print(f"Dear {guest.title()}, please join me for dinner.")
