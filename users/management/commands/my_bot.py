from django.core.management import BaseCommand

from config import settings
from habits.services import send_telegram_message


class Command(BaseCommand):

    def handle(self, *args, **options):
        chat_id = settings.telegram_id  # Здесь должен быть ваш chat_id
        message = "Hello, it's me Daniel. My coursework is great, right?"
        return send_telegram_message(chat_id, message)