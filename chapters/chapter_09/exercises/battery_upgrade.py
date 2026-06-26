"""Exercise 09-09: Battery Upgrade

Summary of the book task:
Add a method that upgrades an electric car battery when needed.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

class Restaurant:
    """A small class used for class-practice exercises."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name.title()} serves {self.cuisine_type}.")

    def set_number_served(self, number):
        self.number_served = number


class User:
    """A small user model for inheritance and method practice."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


restaurant = Restaurant("luna", "tacos")
restaurant.describe_restaurant()
restaurant.set_number_served(42)
print(f"Number served: {restaurant.number_served}")

user = User("ada", "lovelace")
user.describe_user()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
