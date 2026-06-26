"""Exercise 07-05: Movie Tickets

Summary of the book task:
Use a loop and conditionals to report movie ticket prices by age.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

while True:
    age_text = input("Enter your age, or 'quit': ")
    if age_text == "quit":
        break
    age = int(age_text)
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket costs ${price}.")
