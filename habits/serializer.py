
from rest_framework import serializers

from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Habit """

    class Meta:
        model = Habit
        fields = ['id', 'action', 'nice_feeling', 'periodicity', 'last_completed', 'is_public', 'owner']


