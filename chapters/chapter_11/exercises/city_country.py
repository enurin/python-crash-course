"""Exercise 11-01: City, Country

Summary of the book task:
Write a city-country function and a pytest test for the basic output.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def city_country(city, country):
    """Return City, Country."""
    return f"{city.title()}, {country.title()}"

def test_city_country():
    assert city_country("santiago", "chile") == "Santiago, Chile"

if __name__ == "__main__":
    print(city_country("santiago", "chile"))
