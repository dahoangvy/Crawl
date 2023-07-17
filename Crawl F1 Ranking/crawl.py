import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.formula1.com/en/results.html/2023/drivers.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_ = 'resultsarchive-table')
    rows = table.find_all('tr')
    positions = []
    driver_names = []
    nationalitys = []
    cars = []
    points = []

    for row in rows[1:]:
        columns = row.find_all('td')
        position = columns[1].text.strip()
        driver_name = columns[2].text.strip().split('\n')
        driver_name = ' '.join(driver_name[:-1])
        nationality = columns[3].text.strip()
        car = columns[4].text.strip()
        point = columns[5].text.strip()

        positions.append(position)
        driver_names.append(driver_name)
        nationalitys.append(nationality)
        cars.append(car)
        points.append(point)

dict = {'Position': positions,
        'Driver Name': driver_names,
        'Nationality': nationalitys,
        'Car': cars,
        'Points': points}      
df = pd.DataFrame(dict)
df.to_excel('result.xlsx', index=False)