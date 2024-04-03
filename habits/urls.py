from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateApiView, PublicHabitListApiView, HabitListApiView, HabitRetrieveApiView, \
    HabitUpdateApiView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', PublicHabitListApiView.as_view(), name='public_habit'),
    path('habit/', HabitListApiView.as_view(), name='habit_list'),
    path('habit/create/', HabitCreateApiView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', HabitRetrieveApiView.as_view(), name='read_one_habit'),
    path('habit/update/<int:pk>/', HabitUpdateApiView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
