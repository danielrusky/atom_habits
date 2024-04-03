from django.db import models
from config import settings

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

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
