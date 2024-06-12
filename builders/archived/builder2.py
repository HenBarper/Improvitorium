import csv

# 0:title
# 1:id
# 2:tagPages
# 3:tags
# 4:primaryPage
# 5:description

data = []

with open('../data/data.csv', 'r') as file:
  reader = csv.reader(file)
  next(reader)
  for row in reader:
    data.append(row)

# htmlText = 

linkText = f'\t<h1 class="text-center my-3">Test Page</h1>\n'
linkText += f'\t<div class="m-5 games-list">\n'
linkText += f'\t<ul class="py-3">\n'
fullText = f'<div class="m-5">\n\t'
new_file = 'new_file.html'

for item in data:
  linkText += f'<li>\n\t<h5><a href="#{item[1]}">{item[0]}</a></h5>\n</li>\n'
  tags_html = ''
  for tagPage, tag in zip(item[2].split(","), item[3].split(",")): 
    tags_html += f'<a href="{tagPage.strip()}">{tag.strip()}</a> - '
  fullText += f'<!-- ---------- {item[0].upper()} ---------- -->\n'
  fullText += f'<div class="game-box p-2" id="{item[1]}">\n'
  fullText += f'\t<h3>{item[0]}</h3>\n'
  fullText += f'\t<hr>\n'
  fullText += f'\t<p>Description: {item[5]}</p>\n'
  fullText += f'\t<h6>tags</h6>\n'
  fullText += f'\t{tags_html}\n'
  fullText += f'\t<hr>\n'
  fullText += f'\t<h6><a href="#top">Back to Top</a></h6>\n'
  fullText += f'</div>\n\n'
  fullText += f'<hr class="thick-hr">\n\n'

linkText += f'</ul>\n</div>\n\n<hr class="thick-hr">\n\n'
fullText += f'</div>'

existing_file = '../existing_file.html'
with open(existing_file, 'r') as file:
    existing_content = file.read()

# Find insertion point within existing HTML content
insertion_index = existing_content.find('</body>')

# Insert generated content into existing HTML content
new_html_content = existing_content[:insertion_index] + '\n' + linkText + '\n\n' + fullText + '\n' + existing_content[insertion_index:]

# Write updated HTML content to a new file
new_file = '../new_file.html'
with open(new_file, 'w') as file:
    file.write(new_html_content)

# with open(new_file, 'w') as file:
#   file.write(linkText)
#   file.write('\n\n\n\n\n\n')
#   file.write(fullText)