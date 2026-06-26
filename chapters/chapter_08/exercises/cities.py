"""Exercise 08-05: Cities

Summary of the book task:
Write a function that describes a city, using a default country for some calls.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def describe_city(city, country="iceland"):
    """Describe a city and country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city("reykjavik")
describe_city("akureyri")
describe_city("oslo", "norway")
