"""Exercise 08-06: City Names

Summary of the book task:
Write a function that returns a formatted city-country string.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def city_country(city, country):
    """Return a city-country string."""
    return f"{city.title()}, {country.title()}"

print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan"))
print(city_country("oslo", "norway"))
