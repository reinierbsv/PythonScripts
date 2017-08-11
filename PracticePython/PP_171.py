# import libraries
from bs4 import BeautifulSoup
import pandas as pd
import urllib


# specify the url
page = urllib.urlopen("https://www.nytimes.com")

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, "lxml")

# extracting the elements that Im interested in
news = soup.find_all('h2', class_="story-heading")
byline = soup.find_all('p', class_='byline')

# creating nested dictionaries
content = {}
for h in news:
    body = h.find(class_='story-heading').get_text()
    content[h.get_text()] = body
#for b in byline:
#    content[h.p.get_text()]['By'] = b.p[]
print content


#print body
#headings = [h.get_text() for h in body]
#print headings
#titles = pd.DataFrame({
#        "Headlines": headings
#    })
#print titles
