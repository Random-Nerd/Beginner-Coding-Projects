#importing Python Modules
import urllib.request
import bs4
from bs4 import BeautifulSoup as bs

#inserting URL, obtaining HMTL and processing HTML
url=input('enter url: ')
httml = urllib.request.urlopen(url)
raw = httml.read()
soup = bs(raw, 'html.parser')

#writing of the results in a file
filename = input('insert file name: ')
f = open(filename, 'w')
#headers are the description per column
headers = input('input column headers separated by a comma: ')+'\n'
f.write(headers)
#scraping the information needed
#first: separate the division per item or header
#second: scrape the information

section = input('enter section code: ')
attrs = input('enter attribute: ')
code = input('class code: ')
html_section = soup.find_all(section,{attrs:code})
cutouts = html_section[0]
for cutouts in html_section:
	#title must be changed everytime the source changes
	title = cutouts.section.div.div.a.div.div.div.span
	print (title)
#writing of the information in a csv file
	f.write(title + '\n')
f.close()