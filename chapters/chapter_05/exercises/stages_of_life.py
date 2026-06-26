"""Exercise 05-06: Stages of Life

Summary of the book task:
Use an if-elif-else chain to classify a person by stage of life.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

age = 28
if age < 2:
    stage = "baby"
elif age < 4:
    stage = "toddler"
elif age < 13:
    stage = "kid"
elif age < 20:
    stage = "teenager"
elif age < 65:
    stage = "adult"
else:
    stage = "elder"
print(f"This person is a {stage}.")
