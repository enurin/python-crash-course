"""Exercise 05-11: Ordinal Numbers

Summary of the book task:
Print ordinal numbers with the correct suffixes for 1 through 9.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        suffix = "st"
    elif number == 2:
        suffix = "nd"
    elif number == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{number}{suffix}")
