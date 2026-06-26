"""Exercise 03-02: Greetings

Summary of the book task:
Reuse the names list and print a personalized greeting for each person.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

names = ["ada", "grace", "katherine"]
for name in names:
    print(f"Hello, {name.title()}! I hope you are having a good day.")
