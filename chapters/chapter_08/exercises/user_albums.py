"""Exercise 08-08: User Albums

Summary of the book task:
Use a loop to collect album information from the user until they quit.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def make_album(artist, title):
    return {"artist": artist, "title": title}

while True:
    artist = input("Artist, or 'quit': ")
    if artist == "quit":
        break
    title = input("Album title: ")
    print(make_album(artist, title))
