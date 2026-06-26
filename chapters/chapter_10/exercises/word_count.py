from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file"""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path.name} has about {num_words} words.")


filenames = ["alice.txt", "crime_punishment.txt", "moby_dick.txt", "little_women.txt"]
chapter_path = Path(__file__).parents[1]

for filename in filenames:
    path = chapter_path / filename
    count_words(path)
