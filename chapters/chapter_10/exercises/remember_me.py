from pathlib import Path
import json


def get_stored_users(path):
    """Get stored users if possible."""
    if path.exists():
        contents = path.read_text()
        users = json.loads(contents)
        return users
    else:
        return {}


def get_new_user_info():
    """Prompt for new user info."""
    location = input("Where do you live? ")
    hobby = input("What is your favorite hobby? ")

    user_info = {
        "location": location,
        "hobby": hobby,
    }

    return user_info


def greet_user():
    """Greet the user and show the information we remember."""
    path = Path(__file__).with_name("users_info.json")
    users = get_stored_users(path)

    username = input("What is your name? ")

    if username in users:
        user_info = users[username]
        print(f"Welcome back, {username}!")
        print(f"You live in {user_info['location']}.")
        print(f"Your favorite hobby is {user_info['hobby']}.")
    else:
        print("I don't know you yet.")
        user_info = get_new_user_info()
        users[username] = user_info

        contents = json.dumps(users)
        path.write_text(contents)

        print(f"We'll remember you when you come back, {username}!")


greet_user()
