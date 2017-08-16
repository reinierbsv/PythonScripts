# specify the url
quote_page = 'https://www.nytimes.com'

# query the website and return the html to the variable 'page'
page = urlopen(quote_page)

# parse the html using beautiful soap with lxml parser and store in variable `soup`
soup = BeautifulSoup(page, 'lxml')

# finding the content we're interest in. This create a 'list object' stored in  variable 'article'
article = soup.find_all('article', class_="story theme-summary")
heading = []
byline = []

# getting the text from each elements of the list object 'article'
for author in article:
    if author.find(class_='byline'):
        byline.append(author.find(class_='byline').get_text())
for head in article:
    if head.find(class_='byline'):
        heading.append(head.find(class_='story-heading').get_text(strip=True))

# creates a pandas table
titles = pd.DataFrame({
        "Headlines": heading,
        "By": byline
    })
HTML(titles.to_html(classes=[table-striped, table-hover, border-collapse:colapse]))
