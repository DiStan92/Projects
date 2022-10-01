import datetime
import telegram


TOKEN = '5021913485:AAHp33HG3gXsR4Tbhj4ZweklK9nGAxIpuXM'
BOT = telegram.Bot(token=TOKEN)


LINKS = {
    'bot_getUpdate': f'https://api.telegram.org/bot{TOKEN}/getUpdates',
    'nbrb_course': 'https://www.nbrb.by/api/exrates/rates/',
    'nbrb_dinamics': 'https://www.nbrb.by/api/exrates/rates/dynamics/',
    'belarusbank_course': 'https://belarusbank.by/api/kursExchange?city=Лида'
}


def date_interval():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    start_date = '2022-6-1'
    DATE_INTERVAL = f'?startDate={start_date}&endDate={date}'
    return DATE_INTERVAL