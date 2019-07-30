from bs4 import BeautifulSoup
import requests
import csv
import lxml

city = 'Wisconsin, USA'

url = 'https://forecast.weather.gov/MapClick.php?lat=44.6448&lon=-89.7392'

weather_file = 'weather.csv'

req = requests.get(url)

if req.status_code != 200:
    print('something went wrong')
    exit()

lines = []
html_file = req.text
soup = BeautifulSoup(html_file ,'lxml')
for li in soup.find('ul', id='seven-day-forecast-list'):
    lines.append([li.div.find('p', class_='period-name').text , li.div.find('p', class_='temp').text])
    print(li.div.find('p', class_='period-name').text + li.div.find('p', class_='temp').text)

csv.register_dialect('myDialect',
delimiter = ';',
quoting=csv.QUOTE_NONE,
skipinitialspace=True)

with open(weather_file, 'w') as csvFile:
    writer = csv.writer(csvFile, dialect='myDialect')
    writer.writerows(lines)
    print('Done!! Thank you Qazi! simple code, but I will improve it.')
