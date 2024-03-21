import requests

from config import settings


def send_telegram_message(telegram_id, message):
    """Данные для отправки telegram_message пользователю в телеграмме"""

    token = settings.API_TELEGRAM_TOKEN
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': telegram_id,
        'text': message
    }

    response = requests.post(url, data=data)
    response.raise_for_status()