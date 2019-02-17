print('Building site!')
top_html = open('templates/top.html'.read()
middle_html = open('content/index.html').read()
bottom_html=open('templates/bottom.html').read()
combined_html = top_html +middle_html + bottom_html
open('output_file.html',w+10.write(combined.html)
