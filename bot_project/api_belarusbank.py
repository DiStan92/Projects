import requests
from const import LINKS


def api_belarusbank(text_message):
    try:
        result = requests.get(LINKS['belarusbank_course'])
        data = result.json()
        course_in = data[0][str(text_message).upper() + '_in']
        course_out = data[0][str(text_message).upper() + '_out']
        return f'Беларусбанк - {text_message.upper()} is {course_in}/{course_out}\n'
    except KeyError:
        pass