import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

def serialize_animal(animal_info):
    """Return an HTML <li> card for a single animal"""
    output = ""
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_info["name"]}</div>'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal_info['characteristics']['diet']}<br/>\n"
    output += f"<strong>Location:</strong> {animal_info['locations'][0]}<br/>\n"
    if animal_info["characteristics"].get("type"):
        output += f"<strong>Type:</strong> {animal_info['characteristics'].get('type')}<br/>\n"
    output += "</p>\n"
    output += "</li>\n"
    return output

output = ""
for animal_info in animals_data:
    output += serialize_animal(animal_info)



with open("animals_template.html", "r") as file:
    template_html = file.read()


final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(final_html)



