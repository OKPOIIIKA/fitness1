# Generated by Django 5.0.6 on 2024-05-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('title', models.CharField(max_length=50, verbose_name='Направление')),
                ('activity', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='coaches/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренеры',
            },
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='directions/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Вид тренировок',
                'verbose_name_plural': 'Виды тренировок',
            },
        ),
    ]
