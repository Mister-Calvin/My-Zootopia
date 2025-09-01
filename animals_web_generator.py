import json
from tkinter.font import names


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

output = ""
for info in animals_data:
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{info["name"]}</div>'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {info['characteristics']['diet']}<br/>\n"
    output += f"<strong>Location:</strong> {info['locations'][0]}<br/>\n"
    if info["characteristics"].get("type"):
        output += f"<strong>Type:</strong> {info['characteristics'].get('type')}<br/>\n"
    output += "</p>\n"
    output += "</li>\n"

#print(output)


with open("animals_template.html", "r") as file:
    template_html = file.read()

#print(template_html)

final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(final_html)



