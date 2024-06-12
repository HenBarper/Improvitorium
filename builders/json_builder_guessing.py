import json

data = []

# FUNCTION TITLE
def build_guessing_page_json():
    with open('../data/data.json', 'r') as file:
        data.extend(json.load(file))

    htmlText = f'<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    htmlText += f'\t<title>Guessing</title>\n\t<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">\n'
    htmlText += f'\t<link rel="stylesheet" href="../styles/style.css">\n</head>\n'
    htmlText += f'<header id="top">\n\t<div class="d-flex flex-wrap justify-content-around">\n\t\t<a class="mx-5 py-2" href="../index.html">Home</a>\n'
    htmlText += f'\t\t<a class="mx-5 py-2" href="categories.html">Games Exercises and Formats</a>\n\t</div>\n</header>\n<body>'

    # TITLE
    linkText = f'\t<h1 class="text-center my-3">Guessing</h1>\n'
    # SUBTITLE
    linkText += f'\t<p class="text-center my-3">These usually involve one player, the guesser, leaving the room while the other players get suggestions for characters to play. The guesser then has to return and act out some kind of scene with the characters, eventually guessing who they are or what traits they were given based off of hints from the character players.</p>\n'
    linkText += f'\t<div class="m-5 games-list">\n'
    linkText += f'\t\t<ul class="py-3">\n'
    fullText = f'<div class="m-5">\n'

    for item in data:
        # TITLE
        if 'Guessing' in item['tags']:
            linkText += f'\t\t\t<li>\n\t\t\t\t<a href="#{item["id"]}">{item["title"]}</a>\n\t\t\t</li>\n'
            tags_html = ''
            for tagPage, tag in zip(item['tagPages'].split(","), item['tags'].split(",")):
                tags_html += f'<a href="{tagPage.strip()}">{tag.strip()}</a> - '
            fullText += f'\t<!-- ---------- {item["title"].upper()} ---------- -->\n'
            fullText += f'\t<div class="game-box p-2" id="{item["id"]}">\n'
            fullText += f'\t\t<h2>{item["title"]}</h2>\n'
            fullText += f'\t\t<hr>\n'
            for info_key, info_value in item['info'].items():
                fullText += f'\t\t<h3>{info_key}</h3>\n'
                for key in sorted(info_value.keys(), key=int):
                    fullText += f'\t\t{info_value[key]}\n'
            fullText += f'\t\t<h4>Tags</h4>\n'
            fullText += f'\t\t{tags_html}\n'
            fullText += f'\t\t<hr>\n'
            fullText += f'\t\t<h5><a href="#top">Back to Top</a></h5>\n'
            fullText += f'\t</div>\n\n'
            fullText += f'\t<hr class="thick-hr">\n\n'

    linkText += f'\t\t</ul>\n\t</div>\n\n<hr class="thick-hr">'
    fullText += f'</div>'

    htmlEndText = f'</body>\n<footer>\n\t<div class="d-flex flex-wrap justify-content-around">\n'
    htmlEndText += f'\t\t<a class="mx-5 py-2" href="../index.html">Home</a>\n\t\t<a class="mx-5 py-2" href="categories.html">Games Exercises and Formats</a>\n'
    htmlEndText += f'\t</div>\n</footer>\n</html>'

    new_html_content = htmlText + '\n' + linkText + '\n\n' + fullText + '\n' + htmlEndText

    # FILE NAME
    new_file = '../pages/guessing.html'
    with open(new_file, 'w') as file:
        file.write(new_html_content)
