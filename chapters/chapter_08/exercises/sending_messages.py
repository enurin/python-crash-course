"""Exercise 08-10: Sending Messages

Summary of the book task:
Move messages from an unsent list to a sent list inside a function.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(f"Sending: {message}")
        sent_messages.append(message)

messages = ["hello", "keep learning"]
sent_messages = []
send_messages(messages, sent_messages)
print(messages)
print(sent_messages)
