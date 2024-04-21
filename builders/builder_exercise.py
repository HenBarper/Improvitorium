import csv

# 0:title
# 1:id
# 2:tagPages
# 3:tags
# 4:primaryPage
# 5:description

data = []

def build_exercise_page():
  with open('../data/data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
      data.append(row)

  htmlText = f'<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
  htmlText += f'\t<title>Exercises</title>\n\t<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">\n'
  htmlText += f'\t<link rel="stylesheet" href="../styles/style.css">\n</head>\n'
  htmlText += f'<header id="top">\n\t<div class="d-flex flex-wrap justify-content-around">\n\t\t<h5 class="mx-5 py-2"><a href="../index.html">Home</a>\n'
  htmlText += f'\t\t<h5 class="mx-5 py-2"><a href="categories.html">Games Exerciess and Formats</a>\n\t</div>\n</header>\n<body>'

  linkText = f'\t<h1 class="text-center my-3">Exercises</h1>\n'
  linkText += f'\t\t<div class="m-5 games-list">\n'
  linkText += f'\t\t\t<ul class="py-3">\n'
  fullText = f'<div class="m-5">\n'

  for item in data:
    if 'Exercise' in item[3]:
      linkText += f'\t\t\t\t<li>\n\t\t\t\t\t<h5><a href="#{item[1]}">{item[0]}</a></h5>\n\t\t\t\t</li>\n'
      tags_html = ''
      for tagPage, tag in zip(item[2].split(","), item[3].split(",")): 
        tags_html += f'<a href="{tagPage.strip()}">{tag.strip()}</a> - '
      fullText += f'\t<!-- ---------- {item[0].upper()} ---------- -->\n'
      fullText += f'\t<div class="game-box p-2" id="{item[1]}">\n'
      fullText += f'\t\t<h3>{item[0]}</h3>\n'
      fullText += f'\t\t<hr>\n'
      fullText += f'\t\t<p>Description: '
      for character in item[5]:
        if character == '\\':
          fullText += '</p>\n<p>'
        else:
          fullText += character
      # fullText += f'\t\t<p>Description: {item[5]}</p>\n'
      fullText += f'</p>\n'
      fullText += f'\t\t<h6>tags</h6>\n'
      fullText += f'\t\t{tags_html}\n'
      fullText += f'\t\t<hr>\n'
      fullText += f'\t\t<h6><a href="#top">Back to Top</a></h6>\n'
      fullText += f'\t</div>\n\n'
      fullText += f'\t<hr class="thick-hr">\n\n'

  linkText += f'\t\t\t</ul>\n\t\t</div>\n\n<hr class="thick-hr">'
  fullText += f'</div>'

  htmlEndText = f'<p class="white">built</p></body>\n<footer>\n\t<div class="d-flex flex-wrap justify-content-around">\n'
  htmlEndText += f'\t\t<h5 class="mx-5 py-2"><a href="../index.html">Home</a>\n\t\t<h5 class="mx-5 py-2"><a href="categories.html">Games Exerciess and Formats</a>\n'
  htmlEndText += f'\t</div>\n</footer>\n</html>'

  new_html_content = htmlText + '\n' + linkText + '\n\n' + fullText + '\n' + htmlEndText

  new_file = '../pages/exercises.html'
  with open(new_file, 'w') as file:
      file.write(new_html_content)

# build_exercise_page()
