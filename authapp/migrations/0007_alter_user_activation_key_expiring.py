# Generated by Django 3.2 on 2021-08-03 22:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_alter_user_activation_key_expiring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 22, 24, 48, 523149, tzinfo=utc)),
        ),
    ]
