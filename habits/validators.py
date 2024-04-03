from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
    if nice_feeling and not (reward or related_habit):
        raise ValidationError(_('Приятная привычка не может иметь вознаграждения или связанной с ней привычки.'))
