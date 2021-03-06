# Generated by Django 3.2 on 2021-07-28 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0004_alter_user_activation_key_expiring'),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('status', models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен в обработку'), ('PD', 'оплачен'), ('PRD', 'обрабатывается'), ('RDY', 'готов к выдаче'), ('CNC', 'отменен')], default='FM', max_length=3, verbose_name='Статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.user')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='ordersapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Продукт')),
            ],
        ),
    ]
