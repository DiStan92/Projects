import requests
import matplotlib.pyplot as plt
from const import LINKS, date_interval


def api_nbrb(text_message):
    global cur_ID, date, cur_Abbreviation
    try:
        result = requests.get(LINKS['nbrb_course'] + str(text_message) + '?parammode=2')
        data = result.json()
        cur_ID = data.get('Cur_ID')
        date = data.get('Date')[:10]
        cur_Abbreviation = data.get('Cur_Abbreviation')
        cur_Name = data.get('Cur_Name')
        cur_OfficialRate = data.get('Cur_OfficialRate')
        return f'{cur_Name}\nНац. Банк - {cur_Abbreviation} is {cur_OfficialRate}\n'
    except ValueError:
        pass


def api_nbrb_dinamics():
    try:
        result = requests.get(LINKS['nbrb_dinamics'] + str(cur_ID) + date_interval())
        data = result.json()
        date_x = [_['Date'][:10] for _ in data]
        course_y = [_['Cur_OfficialRate'] for _ in data]
        plt.plot(date_x, course_y)
        plt.xlabel('Date')
        plt.ylabel('Course')
        plt.title(cur_Abbreviation)
        plt.savefig('course.png')
        plt.close()
    except ValueError:
        pass