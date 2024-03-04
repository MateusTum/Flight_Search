# Generated by Django 5.0.2 on 2024-03-04 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flights', '0002_alter_city_code_alter_city_population_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoredFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('best_flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='best_flight', to='flights.flight')),
            ],
        ),
    ]
