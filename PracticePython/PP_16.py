# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import csv


# specify the url
quote_page = 'https://www.nytimes.com'

# query the website and return the html to the variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

head = soup.find_all(class_='story-heading')
headings = [h.get_text() for h in head]
titles = pd.DataFrame({
        "Headlines": headings
    })
print(titles)
