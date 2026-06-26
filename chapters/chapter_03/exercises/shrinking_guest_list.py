"""Exercise 03-07: Shrinking Guest List

Summary of the book task:
Shrink the dinner guest list to two people, apologizing to removed guests and clearing the list.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

guests = ["ada", "grace", "alan", "katherine", "margaret", "dorothy"]
print("The new table will not arrive, so I can invite only two people.")
while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry, {removed.title()}, I cannot invite you this time.")
for guest in guests:
    print(f"{guest.title()}, you are still invited.")
del guests[0]
del guests[0]
print(guests)
