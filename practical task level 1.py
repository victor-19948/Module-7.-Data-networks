import requests
from bs4 import BeautifulSoup

page = requests.get('https://mfd.ru/currency/?currency=USD')

soup = BeautifulSoup(page.text, 'html.parser')

mfd_table = soup.find(class_='mfd-table')
all_td = mfd_table.find_all('td')
all_td_text = [item.text for item in all_td]
dates_courses_changes = [all_td_text[i:i + 3] for i in range(0, len(all_td), 3)]
print(dates_courses_changes)
