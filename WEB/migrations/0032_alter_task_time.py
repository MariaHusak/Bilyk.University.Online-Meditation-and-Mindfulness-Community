# Generated by Django 5.0.3 on 2024-04-02 15:20

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('WEB', '0031_remove_profile_profile_picture_alter_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(default=datetime.time(15, 20, 26, 535451)),
        ),
    ]
