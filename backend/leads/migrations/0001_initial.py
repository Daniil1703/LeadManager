# Generated by Django 3.0.6 on 2020-05-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='Email')),
                ('message', models.CharField(blank=True, max_length=500, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
        ),
    ]
