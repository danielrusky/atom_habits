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
            duration='00:01:00',
            action='Тестовое действие',
            nice_feeling=False,
            periodicity=1,
            reward='Тестовое вознаграждение',
            last_completed=datetime.utcnow(),
            is_public=True,
        )

    def test_habit_my_list(self):
        response = self.client.get(reverse('habits:habit_list'))
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
                        "last_completed": self.habit.last_completed.strftime("%Y-%m-%d"),
                        "is_public": self.habit.is_public,
                        "owner": self.habit.owner.id,
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
                "last_completed": self.habit.last_completed.strftime("%Y-%m-%d"),
                "is_public": self.habit.is_public,
                "owner": self.habit.owner.id,
                "place": self.habit.place,
                "duration": self.habit.duration,
                "related_habit": self.habit.related_habit,
                "reward": self.habit.reward
            }
        )

    def test_habit_create(self):
        data = dict(
            owner=self.user.id,
            place='Тестовое место 2',
            duration='00:00:20',
            action='Тестовое действие 2',
            nice_feeling=False,
            periodicity='1',
            reward='Тестовое вознаграждение 2',
            last_completed=datetime.utcnow().strftime("%Y-%m-%d"),
            is_public=True,
        )
        response = self.client.post(reverse('habits:habit_create'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_create_with_related_habit(self):
        habit = Habit.objects.create(
            owner=self.user,
            place='Тестовое место',
            duration='00:00:60',
            action='Тестовое действие',
            nice_feeling=True,
            periodicity=1,
            last_completed=datetime.utcnow(),
            is_public=True,
        )
        data = dict(
            owner=self.user.id,
            place='Тестовое место 2',
            duration='00:00:60',
            action='Тестовое действие 2',
            nice_feeling=False,
            periodicity='1',
            last_completed=datetime.utcnow().strftime("%Y-%m-%d"),
            is_public=True,
            related_habit=habit.id
        )
        response = self.client.post(reverse('habits:habit_create'), data=data)
        self.assertEqual(response.status_code, 201)

    def test_habit_update(self):
        data = dict(
            place='Тестовое место 4',
            duration='00:00:20',
            action='Тестовое действие 4',
            nice_feeling=False,
            periodicity=1,
            reward='Тестовое вознаграждение 4',
            is_public=True,
        )
        response = self.client.patch(reverse('habits:habit_update', args=[self.habit.id]), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "action": data['action'],
                "nice_feeling": data['nice_feeling'],
                "periodicity": data['periodicity'],
                "is_public": data['is_public'],
                "owner": self.habit.owner.id,
                "last_completed": self.habit.last_completed.strftime("%Y-%m-%d"),
                "place": data['place'],
                "duration": data['duration'],
                "related_habit": self.habit.related_habit,
                "reward": data['reward'],
            }
        )

    def test_habit_destroy(self):
        response = self.client.delete(reverse('habits:habit_delete', args=[self.habit.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Habit.objects.count(), 0)
