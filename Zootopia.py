import json
from tkinter.font import names


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

for info in animals_data:
    print(f"Name: {info["name"]}")
    print(f"Diet: {info["characteristics"]["diet"]}")
    print(f"Location: {info["locations"][0]}")
    if info["characteristics"].get("type"):
        print(f"Type: {info["characteristics"].get("type", "")}")
    print()
