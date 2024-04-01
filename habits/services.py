import requests

# from config import settings


class TelegramBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = '7000920511:AAEJN0rRtF7Jw9LIk3k3CLFc92xoL7vbwlM'

    @classmethod
    def send_message(cls, chat_id, text):
        response = requests.post(
            url=f'{cls.URL}{cls.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
        response.raise_for_status()

