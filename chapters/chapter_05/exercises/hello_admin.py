"""Exercise 05-08: Hello Admin

Summary of the book task:
Loop through usernames and print a special greeting for admin.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

usernames = ["admin", "ada", "grace", "alan"]
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
