import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)





def serialize_animal(animal_info):
    """Return an HTML <li> card for a single animal"""
    output = ""
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_info.get('name','Unknown')}</div>'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal_info['characteristics'].get('diet','Unknown')}<br/>\n"
    output += f"<strong>Location:</strong> {animal_info.get('locations',['Unknown'])[0]}<br/>\n"
    if animal_info["characteristics"].get("type","Unknown"):
        output += f"<strong>Type:</strong> {animal_info['characteristics'].get('type','Unknown')}<br/>\n"
    output += "</p>\n"
    output += "</li>\n"
    return output

def generate_html(animals_data):
    output = ""
    for animal_info in animals_data:
        output += serialize_animal(animal_info)
    return output




def write_html(output):
    with open("animals_template.html", "r") as file:
        template_html = file.read()
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", output)
    with open("animalsgettest.html", "w") as file:
        file.write(final_html)



def main():
    animals_data = load_data('animals_data.json')
    write_html(generate_html(animals_data))




if __name__ == "__main__":
    main()
