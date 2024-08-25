import bs4
from bs4 import BeautifulSoup 

file = open("/home/jordan/Bureau/becode/my-repo/Python/advanced/DataWebScrapping/data/becode.html", "r")
print(file.read())
html_doc=file.read()
file.close()
html_doc