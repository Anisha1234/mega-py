import re
import linkGrabber
links = linkGrabber.Links("http://google.com")
htmlpage = links.find(limit=5,pretty=True)
print (htmlpage)