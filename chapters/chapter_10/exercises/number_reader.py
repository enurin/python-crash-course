from pathlib import Path
import json

path = Path(__file__).with_name("numbers.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
