"""Exercise 08-13: User Profile

Summary of the book task:
Use arbitrary keyword arguments to build a user profile dictionary.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

profile = build_profile("ada", "lovelace", field="mathematics", location="london")
print(profile)
