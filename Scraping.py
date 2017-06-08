import requests
from bs4 import BeautifulSoup
import pandas as pd

# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.content)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# print(list(soup.children))
# print([type(item) for item in list(soup.children)])
# html = list(soup.children)[2]
# print(html)
# print(list(html.children))
# body = list(html.children)[3]
# print(body)
# print(list(body.children))
# p = list(body.children)[1]
# print(p)
# print(p.get_text())
# print(soup.find_all('p'))
# print(soup.find_all('p')[0].get_text())
# page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# soup.find_all('p', class_='outer-text') # any p tag that has the class outer-text
# soup.find_all(class_="outer-text") # look for any tag that has the class outer-text
# soup.find_all(id="first") # search for elements by id
# print(soup.select("div p")) # find all the p tags in our page that are inside of a div

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WTdxFWg1-Uk")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
seven_day = soup.find(id='seven-day-forecast-body')
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc")
temp = tonight.find(class_="temp").get_text()

# Adding spaces between strings in short_desc
for r in short_desc:
  if (r.string is None):
    r.string = ' '

print(period)
print(short_desc.get_text())
print(temp)

# extract the title attribute from the img tag
img = tonight.find("img")
desc = img['title']

print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(short_descs)
print(temps)
print(descs)

weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
        "desc":descs
    })

print(weather)