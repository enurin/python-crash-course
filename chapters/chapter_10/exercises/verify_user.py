"""Exercise 10-14: Verify User

Summary of the book task:
Verify whether the stored user is the current user and update the file if needed.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == "y":
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    #   Prompt for a new username.
    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")


greet_user()
