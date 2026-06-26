"""Exercise 03-10: Every Function

Summary of the book task:
Use several list operations and functions in one small program.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

languages = ["python", "javascript", "rust", "go"]
languages.append("ruby")
languages.insert(1, "c")
print(sorted(languages))
print(len(languages))
removed = languages.pop()
print(f"Removed: {removed}")
print(languages)
