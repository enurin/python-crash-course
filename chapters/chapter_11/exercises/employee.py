"""Exercise 11-03: Employee

Summary of the book task:
Create an Employee class and test default and custom raises.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

class Employee:
    """Represent an employee."""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

def test_give_default_raise():
    employee = Employee("ada", "lovelace", 50_000)
    employee.give_raise()
    assert employee.salary == 55_000

def test_give_custom_raise():
    employee = Employee("ada", "lovelace", 50_000)
    employee.give_raise(10_000)
    assert employee.salary == 60_000
