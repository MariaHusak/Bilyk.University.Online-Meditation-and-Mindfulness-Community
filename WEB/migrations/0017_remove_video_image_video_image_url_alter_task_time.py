# Generated by Django 5.0.3 on 2024-03-30 15:53

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('WEB', '0016_alter_task_time_alter_video_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='image',
        ),
        migrations.AddField(
            model_name='video',
            name='image_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(default=datetime.time(15, 53, 11, 729199)),
        ),
    ]
