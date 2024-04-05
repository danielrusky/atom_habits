from rest_framework import serializers

from .models import Habit
from .validators import validate_reward_and_habit, \
    validate_enjoyable_habit_without_reward_or_association, \
    validate_pleasant_habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Habit """

    class Meta:
        model = Habit
        fields = ['id', 'action', 'nice_feeling', 'periodicity',
                  'last_completed', 'is_public', 'owner', 'place', 'duration',
                  'related_habit', 'reward']

    def validate(self, data):
        if not data.get('related_habit'):
            return data
        # Проверка одновременного заполнения полей вознаграждение и связанная_привычка
        validate_reward_and_habit(
            data['reward'], data['related_habit']
        )
        # Проверка того, что связанная привычка имеет признак приятной_привычки.
        validate_pleasant_habit(
            data['related_habit'],
            data['related_habit'].nice_feeling if self.related_habit else False
        )
        # Проверка того, что приятная привычка не может иметь награды или связанной с ней приятной_привычки.
        validate_enjoyable_habit_without_reward_or_association(
            data['nice_feeling'], data['reward'], data['related_habit']
        )
        return data


class HabitListSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Habit """

    class Meta:
        model = Habit
        fields = ['id', 'action', 'nice_feeling', 'periodicity',
                  'last_completed', 'is_public', 'owner']
