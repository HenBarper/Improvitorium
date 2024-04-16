import csv

# 0:title
# 1:id
# 2:tagPages
# 3:tags
# 4:description

data = []

with open('data.csv', 'r') as file:
  reader = csv.reader(file)
  next(reader)
  for row in reader:
    data.append(row)

linkText = ''
fullText = ''
new_file = 'new_file.html'

for item in data:
  linkText += f'<li>\n\
\t<h5><a href="#{item[1]}">{item[0]}</a>\n\
</h5></li>\n'
  tags_html = ''
  for tagPage, tag in zip(item[2].split(","), item[3].split(",")): 
    tags_html += f'<a href="{tagPage.strip()}">{tag.strip()}</a> - '
  fullText += f'<!-- ---------- {item[0].upper()} ---------- -->\n\
<div class="game-box p-2" id="{item[0]}">\n\
\t<h3>{item[0]}</h3>\n\
\t<hr>\n\
\t<p>{item[4]}</p>\n\
\t<h6>tags</h6>\n\
\t{tags_html}\n\
\t<hr>\n\
\t<h6><a href="#top">Back to Top</a></h6>\n\
</div>\n\n\
<hr class="thick-hr">\n\n'

with open(new_file, 'w') as file:
  file.write(linkText)
  file.write('\n\n\n\n\n\n')
  file.write(fullText)