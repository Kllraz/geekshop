# Generated by Django 3.2 on 2021-07-28 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210727_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expiring',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 30, 9, 13, 36, 838746, tzinfo=utc)),
        ),
    ]
