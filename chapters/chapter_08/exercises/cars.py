"""Exercise 08-14: Cars

Summary of the book task:
Write a function that builds a car dictionary with flexible options.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def make_car(manufacturer, model, **options):
    options["manufacturer"] = manufacturer
    options["model"] = model
    return options

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
