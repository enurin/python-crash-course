"""Exercise 06-05: Rivers

Summary of the book task:
Store major rivers and countries in a dictionary and loop through keys and values.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

rivers = {"nile": "egypt", "amazon": "brazil", "danube": "germany"}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print(list(rivers.keys()))
print(list(rivers.values()))
