# Generated by Django 3.2 on 2021-07-31 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_user_activation_key_expiring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 2, 12, 58, 45, 670348, tzinfo=utc)),
        ),
    ]
