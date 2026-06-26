"""Exercise 05-10: Checking Usernames

Summary of the book task:
Check new usernames against existing usernames without caring about capitalization.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

current_users = ["ada", "Grace", "alan", "eric", "admin"]
new_users = ["grace", "maria", "Admin", "sara", "tom"]
current_users_lower = [user.lower() for user in current_users]
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} is already taken.")
    else:
        print(f"{user} is available.")
