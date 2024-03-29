from datetime import timedelta
from django.core.validators import MaxValueValidator
from django.db import models
from config import settings
from habits.validators import validate_reward_and_habit, validate_pleasant_habit, \
    validate_enjoyable_habit_without_reward_or_association

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """ Модель полезной привычки """
    action = models.CharField(max_length=255, verbose_name='Действие')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Владелец', null=True)
    nice_feeling = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    periodicity = models.IntegerField(default=7, verbose_name='Периодичность выполнения привычки')
    last_completed = models.DateField(verbose_name='Последний срок', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")
    place = models.CharField(max_length=255, verbose_name='Место действия')
    duration = models.DurationField(verbose_name='Время выполнения привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    reward = models.CharField(max_length=255, verbose_name='Вознаграждение', **NULLABLE)

    def __str__(self):
        return f'{self.action}'

    def clean(self):
        # Проверка одновременного заполнения полей вознаграждение и связанная_привычка
        validate_reward_and_habit(self.reward, self.related_habit)

        # Проверка того, что связанная привычка имеет признак приятной_привычки.
        validate_pleasant_habit(self.related_habit, self.related_habit.nice_feeling if self.related_habit else False)

        # Проверка того, что приятная привычка не может иметь награды или связанной с ней приятной_привычки.
        validate_enjoyable_habit_without_reward_or_association(self.nice_feeling, self.reward, self.related_habit)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'



