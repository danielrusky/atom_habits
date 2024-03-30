# Generated by Django 4.2.11 on 2024-03-28 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="duration",
            field=models.DurationField(
                blank=True, null=True, verbose_name="Время выполнения привычки"
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="place",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Место действия"
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="related_habit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="habits.habit",
                verbose_name="Связанная привычка",
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="reward",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Вознаграждение"
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="nice_feeling",
            field=models.BooleanField(
                default=False, verbose_name="Признак приятной привычки"
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.IntegerField(
                default=7, verbose_name="Периодичность выполнения привычки"
            ),
        ),
        migrations.DeleteModel(
            name="Feeling",
        ),
    ]