import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?textField1=39.96&textField2=-75.27#.Xjtzd2hKhPY'
)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
#page source will print

week = soup.find(id='seven-day-forecast-body')
#print(week)
#it will print specific div tag where above id is available not full page

items = week.find_all_next(class_='tombstone-container')
#print(items)

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]
print(period_names)
print(short_desc)
print(temp)

weather_stuff = pd.DataFrame(
    {'period': period_names,
     'short_desc': short_desc,
     'temp': temp
     })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
