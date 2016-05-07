from bs4 import BeautifulSoup
import urllib
htmlpage = urllib.urlopen("http://xtasy.cetb.in").read()
soup = BeautifulSoup(htmlpage)
links = []
links = soup.findAll('a')
for link in links:
	print link['href']