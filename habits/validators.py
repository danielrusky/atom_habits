from datetime import timedelta

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from habits.models import Habit


def validate_reward_and_habit(reward, related_habit):
    """Проверка одновременного заполнения полей вознаграждение и связанная_привычка"""
    if reward and related_habit:
        raise ValidationError(_('Вы не можете указать вознаграждение и связанную с ним привычку одновременно.'))


def validate_pleasant_habit(related_habit, nice_feeling):
    """Проверка того, что связанная привычка имеет признак приятной_привычки."""
    if related_habit and not nice_feeling:
        raise ValidationError(
            _('Сопутствующими привычками могут быть только те, которые имеют характеристики приятной привычки.'))


def validate_enjoyable_habit_without_reward_or_association(nice_feeling, reward, related_habit):
    """Проверка того, что приятная привычка не может иметь награды или связанной с ней привычки."""
    try:
        if nice_feeling:
            if related_habit or reward:
                raise ValidationError(
                    _('Приятная привычка не может иметь вознаграждения или связанной с ней привычки.'))
    except KeyError:
        pass


def validate_time_habit(duration):
    time = timedelta(minutes=2)
    if duration > time:
        raise ValidationError('Привычку можно выполнять не более 120 секунд')

