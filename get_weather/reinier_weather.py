import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://www.cbc.ca/montreal/weather/s0000635.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

summary = soup.find('div', id="wt-right")

period_tags = summary.select("div h3")
periods = [pt.get_text() for pt in period_tags]
short_descs =  summary.select("div p")
description = [summary.find("span", class_="wt-subtitle celsius").get_text()] + [sd.get_text() for sd in short_descs]

print(periods)
print(description)

weather = pd.DataFrame({
        "short_desc": description,
        "period": periods
    })
print(weather)
