"""Exercise 08-11: Archived Messages

Summary of the book task:
Send a copy of a message list so the original list stays unchanged.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def send_messages(messages, sent_messages):
    while messages:
        sent_messages.append(messages.pop())

messages = ["hello", "keep learning"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Original:", messages)
print("Sent:", sent_messages)
