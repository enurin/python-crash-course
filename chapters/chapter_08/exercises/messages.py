"""Exercise 08-09: Messages

Summary of the book task:
Pass a list of messages to a function and print each message.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def show_messages(messages):
    for message in messages:
        print(message)

messages = ["hello", "keep learning", "functions are useful"]
show_messages(messages)
