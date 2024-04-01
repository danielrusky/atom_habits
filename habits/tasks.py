from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from config.celery import app
from .models import Habit
from .services import TelegramBot


@app.task
def check_habits_and_send_reminders():
    today = timezone.now().date()
    habits = Habit.objects.select_related('owner').all()
    for habit in habits:
        if habit.last_completed > today:
            send_email_reminder(habit.owner, habit)
            send_telegram_reminder(habit.owner, habit)


def send_email_reminder(user, habit):
    send_mail(
        subject='Время завершить свою привычку!',
        message=f'Пришло время выполнить свою привычку: {habit.action}.'
                f'Вы устанавливаете, что это должно быть сделано каждый {habit.periodicity} день.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )


def send_telegram_reminder(user, habit):
    if user.telegram_chat_id:
        message = f'Пришло время выполнить свою привычку: {habit.action}.' \
                  f'Вы установили, что это будет происходить каждые {habit.periodicity} дней.'
        TelegramBot.send_message(user.telegram_chat_id, message)
