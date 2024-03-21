from django.contrib import admin

from habits.models import Habit, Feeling


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'action', 'nice_feeling', 'periodicity', 'last_completed', 'is_public')


@admin.register(Feeling)
class FeelingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'place', 'action', 'nice_feeling', 'frequency', 'reward', 'time_to_complete')