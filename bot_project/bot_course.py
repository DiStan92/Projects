import requests
import pprint
from const import BOT, LINKS
from api_nbrb import api_nbrb, api_nbrb_dinamics
from api_belarusbank import api_belarusbank


pp = pprint.PrettyPrinter(indent=4)

def bot_course():
    last_update_id = 0
    while True:
        result = requests.get(LINKS['bot_getUpdate'], params={'offset': last_update_id + 1})
        data = result.json()
        pp.pprint(data)
        res = data['result']
        if not res:
            pass
        else:
            text_message = res[0]['message']['text']
            print(text_message)

        for update in data['result']:
            last_update_id = update['update_id']
            chat_id = update['message']['chat']['id']
            try:
                courses = api_nbrb(text_message) + api_belarusbank(text_message)
                api_nbrb_dinamics()
                send_result = BOT.send_message(chat_id=chat_id, text=courses)
                image = open('course.png', 'rb')
                send_photo = BOT.sendPhoto(chat_id=chat_id, photo=image)
            except TypeError:
                send_result = BOT.send_message(chat_id=chat_id, text='input correct message')

bot_course()