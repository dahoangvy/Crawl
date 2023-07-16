from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl

browser = webdriver.Chrome()
browser.get('https://www.fifa.com/fifa-world-ranking/men?dateId=id12189')

browser.implicitly_wait(5)
btn_acept = browser.find_element(By.ID, "onetrust-reject-all-handler")
btn_acept.click()

ranks = []
teams = []
points = []

table = browser.find_element(By.CLASS_NAME, 'table_rankingTable__7gmVl')
rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    rank = cells[0].text
    team = cells[2].text
    point = cells[3].text
    ranks.append(rank)
    teams.append(team)
    points.append(point)

dict = {'Ranks': ranks, 'Team': teams, 'PTS': points}
df = pd.DataFrame(dict)
df.to_excel('BXH.xlsx', index=False)
