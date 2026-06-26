"""Exercise 11-02: Population

Summary of the book task:
Add optional population support while keeping the original city-country test passing.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def city_country(city, country, population=None):
    """Return a formatted city string, with optional population."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    return result

def test_city_country():
    assert city_country("santiago", "chile") == "Santiago, Chile"

def test_city_country_population():
    assert city_country("santiago", "chile", 5_000_000) == "Santiago, Chile - population 5000000"
