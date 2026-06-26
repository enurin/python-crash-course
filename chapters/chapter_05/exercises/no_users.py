"""Exercise 05-09: No Users

Summary of the book task:
Handle an empty usernames list with an if test.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

usernames = []
if usernames:
    for username in usernames:
        print(f"Hello {username.title()}!")
else:
    print("We need to find some users!")
