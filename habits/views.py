from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializer import HabitSerializer, HabitListSerializer


class PublicHabitListApiView(generics.ListAPIView):
    """ Список общественных привычек """
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitListApiView(generics.ListAPIView):
    """ Список привычек """
    serializer_class = HabitListSerializer
    pagination_class = HabitPaginator
    # permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user.id).order_by('id')


class HabitCreateApiView(generics.CreateAPIView):
    """ Создание привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """ Чтение одной привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitUpdateApiView(generics.UpdateAPIView):
    """ Обновление привычки """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычек """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]