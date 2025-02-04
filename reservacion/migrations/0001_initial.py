# Generated by Django 5.1.3 on 2024-11-14 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='lugares.lugar')),
            ],
        ),
    ]
