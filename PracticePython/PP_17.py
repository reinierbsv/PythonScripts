# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import csv


# specify the url
quote_page = 'https://www.nytimes.com'

# query the website and return the html to the variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soap with lxml parser and store in variable `soup`
soup = BeautifulSoup(page, 'lxml')

# finding the content we're interest in. This create a 'list object' stored in  variable 'head'
head = soup.find_all('h2', class_="story-heading")
by = soup.find_all('p', class_='byline')

# getting the text from each elements of the list object 'head'
headings = [h.get_text(strip=True).strip() for h in head]

# creates a pandas table and print it
titles = pd.DataFrame({
        "Headlines": headings
    })
print(titles)
