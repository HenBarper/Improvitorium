import json

data = []

def build_exercise_page_json():
    with open('../data/data.json', 'r') as file:
        data.extend(json.load(file))

    htmlText = f'<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    htmlText += f'\t<title>Exercises</title>\n\t<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">\n'
    htmlText += f'\t<link rel="stylesheet" href="../styles/style.css">\n</head>\n'
    htmlText += f'<header id="top">\n\t<div class="d-flex flex-wrap justify-content-around">\n\t\t<h5 class="mx-5 py-2"><a href="../index.html">Home</a></h5>\n'
    htmlText += f'\t\t<h5 class="mx-5 py-2"><a href="categories.html">Games Exercises and Formats</a></h5>\n\t</div>\n</header>\n<body>'

    linkText = f'\t<h1 class="text-center my-3">Exercises</h1>\n'
    linkText += f'\t<p class="text-center my-3">These exercises are meant to develop various improvisational skills.</p>\n'
    linkText += f'\t<div class="m-5 games-list">\n'
    linkText += f'\t\t<ul class="py-3">\n'
    fullText = f'<div class="m-5">\n'

    for item in data:
        if 'Exercise' in item['tags']:
            linkText += f'\t\t\t<li>\n\t\t\t\t<h5><a href="#{item["id"]}">{item["title"]}</a></h5>\n\t\t\t</li>\n'
            tags_html = ''
            for tagPage, tag in zip(item['tagPages'].split(","), item['tags'].split(",")):
                tags_html += f'<a href="{tagPage.strip()}">{tag.strip()}</a> - '
            fullText += f'\t<!-- ---------- {item["title"].upper()} ---------- -->\n'
            fullText += f'\t<div class="game-box p-2" id="{item["id"]}">\n'
            fullText += f'\t\t<h3>{item["title"]}</h3>\n'
            fullText += f'\t\t<hr>\n'
            if item.get('description'):
              for character in item['description']:
                  fullText += character
            if item.get('example'):
              for character in item['example']:
                  fullText += character
            if item.get('purpose'):
              for character in item['purpose']:
                  fullText += character
            if item.get('tips'):
              for character in item['tips']:
                  fullText += character
            if item.get('source'):
              for character in item['source']:
                  fullText += character
            fullText += f'\t\t<h6>Tags</h6>\n'
            fullText += f'\t\t{tags_html}\n'
            fullText += f'\t\t<hr>\n'
            fullText += f'\t\t<h6><a href="#top">Back to Top</a></h6>\n'
            fullText += f'\t</div>\n\n'
            fullText += f'\t<hr class="thick-hr">\n\n'

    linkText += f'\t\t</ul>\n\t</div>\n\n<hr class="thick-hr">'
    fullText += f'</div>'

    htmlEndText = f'</body>\n<footer>\n\t<div class="d-flex flex-wrap justify-content-around">\n'
    htmlEndText += f'\t\t<h5 class="mx-5 py-2"><a href="../index.html">Home</a></h5>\n\t\t<h5 class="mx-5 py-2"><a href="categories.html">Games Exercises and Formats</a></h5>\n'
    htmlEndText += f'\t</div>\n</footer>\n</html>'

    new_html_content = htmlText + '\n' + linkText + '\n\n' + fullText + '\n' + htmlEndText

    new_file = '../pages/exercises.html'
    with open(new_file, 'w') as file:
        file.write(new_html_content)
