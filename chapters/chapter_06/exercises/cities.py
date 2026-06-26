"""Exercise 06-11: Cities

Summary of the book task:
Store city facts in nested dictionaries and print the information.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

cities = {"tokyo": {"country": "japan", "population": 37_000_000}, "oslo": {"country": "norway", "population": 700_000}}
for city, info in cities.items():
    print(f"{city.title()} is in {info['country'].title()} and has about {info['population']} people.")
