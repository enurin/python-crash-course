"""Exercise 03-04: Guest List

Summary of the book task:
Create a dinner guest list and print invitations to each guest.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

guests = ["ada lovelace", "grace hopper", "alan turing"]
for guest in guests:
    print(f"Dear {guest.title()}, please join me for dinner.")
