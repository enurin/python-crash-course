"""Exercise 07-07: Infinity

Summary of the book task:
Recognize what makes an infinite loop and keep this practice version safe to run.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

# This is a safe demonstration. A real infinite loop would keep running forever.
count = 0
while count < 3:
    print("This loop would be infinite without the count update.")
    count += 1
