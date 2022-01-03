import requests
from bs4 import BeautifulSoup
import webbrowser

page = requests.get("https://forecast.weather.gov/MapClick.php?x=201&y=205&site=vef&zmx=&zmy=&map_x=201&map_y=205#.Yc5PPS-B0_U")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id = "seven-day-forecast")
forecast_items = seven_day.find_all(class_='tombstone-container')
tonight = forecast_items[0]
#print(tonight.prettify())
period = tonight.find(class_= "period-name").get_text()
short_desc = tonight.find(class_= "short-desc").get_text()
temp = tonight.find(class_= "temp").get_text()
print(period)
print(short_desc)
print(temp)
img = tonight.find("img")
desc = img['title']
print(desc)
