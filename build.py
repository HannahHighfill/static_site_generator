print('Building Home page')
top_html = open('templates/top.html').read()
middle_html = open('content/home.html').read()
bottom_html = open('templates/bottom.html').read()
combined_html = top_html + middle_html + bottom_html
open('docs/index.html',"w+").write(combined_html)

print('Building Blog page')
top_html = open('templates/top.html').read()
middle_html = open('content/blog.html').read()
bottom_html=open('templates/bottom.html').read()
combined_html = top_html +middle_html + bottom_html
open('docs/blog.html',"w+").write(combined_html)

print('Building projects page')
top_html = open('templates/top.html').read()
middle_html = open('content/projects.html').read()
bottom_html=open('templates/bottom.html').read()
combined_html = top_html +middle_html + bottom_html
open('docs/projects.html',"w+").write(combined_html)
