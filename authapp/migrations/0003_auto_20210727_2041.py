# Generated by Django 3.2 on 2021-07-27 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_user_activation_key_expiring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 29, 17, 41, 55, 285658, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Мужской'), ('W', 'Женский')], max_length=1, verbose_name='пол'),
        ),
    ]
