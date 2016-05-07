import urllib
htmlfile = urllib.urlopen("http://gogle.com")
htmltext = htmlfile.read()
print htmltext