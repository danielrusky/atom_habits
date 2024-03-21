
from rest_framework import serializers

from .models import Habit, Feeling


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Habit """

    class Meta:
        model = Habit
        fields = ['id', 'action', 'nice_feeling', 'periodicity', 'last_completed', 'is_public', 'owner']


class FeelingSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Feeling """

    # изменение формата времени и даты для поля action_time в модели Feeling
    action_datatime = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Feeling
        fields = ['id', 'place', 'action', 'nice_feeling', 'frequency', 'time_to_complete', 'user',
                  'related_habit', 'action_datatime']
