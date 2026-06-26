"""Exercise 03-08: Seeing the World

Summary of the book task:
Practice temporary and permanent sorting with a list of places you would like to visit.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

places = ["japan", "norway", "new zealand", "peru", "iceland"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
