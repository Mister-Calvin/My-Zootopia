import json
from tkinter.font import names


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

output = ""
for info in animals_data:
    output += (f"Name: {info["name"]}\n")
    output += (f"Diet: {info["characteristics"]["diet"]}\n")
    output += (f"Location: {info["locations"][0]}\n")
    if info["characteristics"].get("type"):
        output += (f"Type: {info["characteristics"].get("type", "")}\n")
    output += "\n"

#print(output)


with open("animals_template.html", "r") as file:
    template_html = file.read()

#print(template_html)

final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(final_html)



