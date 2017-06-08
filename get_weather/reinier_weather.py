import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://meteo.gc.ca/city/pages/qc-147_metric_f.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

seven_day = soup.find('table', class_="table-condensed")
forecast_items = seven_day.find_all('p', class_="mrgn-bttm-0")
period = seven_day.find_all('th')

#print(seven_day)
#print(forecast_items)
print(period)
