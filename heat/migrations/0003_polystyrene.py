# Generated by Django 4.2.4 on 2023-09-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heat', '0002_rename_buildingpartition_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polystyrene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_polystyrene', models.CharField(max_length=100)),
                ('thickness', models.FloatField()),
                ('thermal_conductivity', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
    ]