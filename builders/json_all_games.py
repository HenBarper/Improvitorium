import json
import string

def build_all_games_page(data_file='../data/data.json', output_file='../pages/all_games.html'):
    data = []

    # Load data from the JSON file
    with open(data_file, 'r') as file:
        data.extend(json.load(file))

    # Base HTML structure for the All Games & Exercises page
    html_text = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Games & Exercises</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../styles/style.css">
</head>
<header id="top">\n\t<div class="d-flex flex-wrap justify-content-around">\n\t\t<a class="mx-5 py-2" href="../index.html">Home</a><a class="mx-5 py-2" href="categories.html">Games Exercises and Formats</a>\n\t</div>\n</header>
<body>
  <h1 class="text-center" id="top">All Games & Exercises</h1>
  <div class="mt-5 text-center">
    <a href="#numbers">#</a> 
""" + " ".join([f'<a href="#{letter}">{letter.upper()}</a>' for letter in string.ascii_lowercase]) + """
  </div>
  <div class="m-5">
"""

    # Create placeholders for each alphabet letter section and numbers
    alphabet_sections = {letter: [] for letter in string.ascii_lowercase}
    number_section = []

    # Sort and categorize the games by their starting character
    for item in data:
        # Ensure 'title' exists, is a string, and is non-empty
        if 'title' in item and isinstance(item['title'], str) and len(item['title']) > 0:
            first_char = item['title'][0]
            if first_char.isdigit():
                number_section.append(f'<li><h5><a href="{item["primary_page"]}">{item["title"]}</a></h5></li>')
            elif first_char.lower() in alphabet_sections:
                alphabet_sections[first_char.lower()].append(f'<li><h5><a href="{item["primary_page"]}">{item["title"]}</a></h5></li>')

    # Add the numbers section if it contains items
    if number_section:
        html_text += """
    <h3 id="numbers">Numbers</h3>
    <div>
      <ul>
""" + "\n".join(number_section) + """
      </ul>
    </div>
"""

    # Populate the HTML with the categorized games
    for letter in string.ascii_lowercase:
        html_text += f'    <h3 id="{letter}">{letter.upper()}</h3>\n    <div>\n'
        if alphabet_sections[letter]:
            html_text += '      <ul>\n' + '\n'.join(alphabet_sections[letter]) + '\n      </ul>\n'
        html_text += '    </div>\n'

    # Close the HTML structure
    html_text += """
    <h5><a href="#top">Back to Top</a></h5>
  </div>
  <footer>\n\t<div class="d-flex flex-wrap justify-content-around"><a class="mx-5 py-2" href="../index.html">Home</a>\n\t\t<a class="mx-5 py-2" href="categories.html">Games Exercises and Formats</a></div>\n</footer>\
</body>
</html>
"""

    # Write the generated HTML to the output file
    with open(output_file, 'w') as file:
        file.write(html_text)

    print(f"{output_file} has been created.")

# Example usage
build_all_games_page()
