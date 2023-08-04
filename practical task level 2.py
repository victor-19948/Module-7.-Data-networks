import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page = requests.get('https://mfd.ru/currency/?currency=USD')

soup = BeautifulSoup(page.text, 'html.parser')

mfd_table = soup.find(class_='mfd-table')

# список из всех тегов 'td'
all_td = mfd_table.find_all('td')

# список всех дат в обратном порядке (по возрастанию)
dates = [item.text for item in all_td[len(all_td)-3::-3]]

# список всех курсов в обратном порядке (по возрастанию)
courses = [float(item.text) for item in all_td[len(all_td)-2::-3]]

# создание графика x - dates, y - courses
plt.plot(dates, courses)

# деление списка с датами на условные 5 частей иначе даты накладываются друг на друга (точка 0, и 4 кусочка)
t = len(dates)//4

# делаем метки по координате x соответствующие позициям
x_ticks = [i for i in range(len(dates))[::t]]

# добавляем на метки соответствующие даты из списка dates
x_labels = [dates[i] for i in x_ticks]

# отображение новых дат не наезжающих друг на друга
plt.xticks(ticks=x_ticks, labels=x_labels)

# названия
plt.title('Курс доллара')
plt.gca().set_xlabel("Дата")
plt.gca().set_ylabel("руб.")

# отображение графика
plt.show()
