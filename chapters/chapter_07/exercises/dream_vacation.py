"""Exercise 07-10: Dream Vacation

Summary of the book task:
Poll users about dream vacation locations and print the collected responses.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

responses = {}
while True:
    name = input("What is your name? ")
    place = input("If you could visit one place, where would you go? ")
    responses[name] = place
    repeat = input("Would another person like to respond? (yes/no) ")
    if repeat == "no":
        break
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
