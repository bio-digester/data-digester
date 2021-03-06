# Generated by Django 2.0.5 on 2018-05-09 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biodigester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('water_flow', models.FloatField(blank=True, default=None)),
                ('temperature', models.FloatField(blank=True, default=None)),
                ('internal_pressure', models.FloatField(blank=True, default=None)),
                ('ph', models.FloatField(blank=True, default=None)),
                ('gas_production', models.FloatField(blank=True, default=None)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
