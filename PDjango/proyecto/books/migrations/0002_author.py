# Generated by Django 4.0.1 on 2022-03-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=120, verbose_name='Apellido')),
                ('birtg_Date', models.DateField(verbose_name='Fecha nacimiento')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'db_table': 'authors',
            },
        ),
    ]
