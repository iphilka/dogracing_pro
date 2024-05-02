# Generated by Django 5.0.4 on 2024-05-02 11:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('breed', models.CharField(choices=[])),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')])),
                ('tatoo', models.CharField(max_length=15)),
                ('microchip_number', models.CharField(max_length=30)),
                ('rkf_number', models.CharField(max_length=15)),
                ('qualification_book_number', models.CharField(max_length=20)),
            ],
        ),
    ]
