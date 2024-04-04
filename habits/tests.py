from datetime import datetime

from django.urls import reverse
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.user.set_password('test_pass123')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place='Тестовое место',
            duration='15:00:00',
            action='Тестовое действие',
            nice_feeling=False,
            periodicity='1',
            reward='Тестовое вознаграждение',
            last_completed=datetime.utcnow(),
            is_public=True,
        )

    def test_habit_my_list(self):
        response = self.client.get(reverse('habits:habits'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        "id": self.habit.id,
                        "action": self.habit.action,
                        "nice_feeling": self.habit.nice_feeling,
                        "periodicity": self.habit.periodicity,
                        "last_completed": self.habit.last_completed,
                        "is_public": self.habit.is_public,
                        "owner": self.habit.owner,
                        "place": self.habit.place,
                        "duration": self.habit.duration,
                        "related_habit": self.habit.related_habit,
                        "reward": self.habit.reward
                    }
                ]
            }
        )

    def test_habit_detail(self):
        response = self.client.get(reverse('habits:read_one_habit', args=[self.habit.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "action": self.habit.action,
                "nice_feeling": self.habit.nice_feeling,
                "periodicity": self.habit.periodicity,
                "last_completed": self.habit.last_completed,
                "is_public": self.habit.is_public,
                "owner": self.habit.owner,
                "place": self.habit.place,
                "duration": self.habit.duration,
                "related_habit": self.habit.related_habit,
                "reward": self.habit.reward
            }
        )

    def test_habit_create(self):
        data = dict(
            owner=self.user,
            place='Тестовое место 2',
            duration='15:00:00',
            action='Тестовое действие 2',
            nice_feeling=False,
            periodicity='1',
            reward='Тестовое вознаграждение 2',
            last_completed=datetime.utcnow(),
            is_public=True,
        )
        response = self.client.post(reverse('habits:habit_create'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_validation(self):
        data = dict(
            owner=self.user,
            place='Тестовое место 3',
            duration='15:00:00',
            action='Тестовое действие 3',
            nice_feeling=True,
            periodicity='1',
            reward='Тестовое вознаграждение 3',
            last_completed=datetime.utcnow(),
            is_public=True,
        )
        response = self.client.post(reverse('habits:habit_create'), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
                         {'ValidationError': [
                             'Приятная привычка не может иметь вознаграждения или связанной с ней привычки.']})

    def test_habit_update(self):
        data = dict(
            owner=self.user,
            place='Тестовое место 4',
            duration='15:00:00',
            action='Тестовое действие 4',
            nice_feeling=False,
            periodicity='1',
            reward='Тестовое вознаграждение 4',
            last_completed=datetime.utcnow(),
            is_public=True,
        )
        response = self.client.put(reverse('habits:habit_update', args=[self.habit.id]), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'place': data['place'],
                'time': data['time'],
                'action': data['action'],
                'is_pleasant': data['is_pleasant'],
                'foreign_habit': self.habit.foreign_habit,
                'period': data['period'],
                'reward': self.habit.reward,
                'time_to_complete': data['time_to_complete'],
                'is_public': data['is_public'],
            }
        )

    def test_habit_destroy(self):
        response = self.client.delete(reverse('habits:habit_delete', args=[self.habit.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Habit.objects.count(), 0)
