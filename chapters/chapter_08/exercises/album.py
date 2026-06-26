"""Exercise 08-07: Album

Summary of the book task:
Return album information in a dictionary, with an optional song count.

Run this file directly with Python. The solution is intentionally beginner-friendly
and focuses on the concepts introduced by this point in the book.
"""

def make_album(artist, title, songs=None):
    """Return a dictionary describing an album."""
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print(make_album("nina simone", "little girl blue"))
print(make_album("miles davis", "kind of blue", 5))
