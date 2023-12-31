# Generated by Django 4.2.4 on 2023-09-30 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heat', '0005_thermalisolation_delete_polystyrene'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='material',
            name='thermal_conductivity',
        ),
        migrations.RemoveField(
            model_name='material',
            name='thickness',
        ),
        migrations.AlterField(
            model_name='thermalisolation',
            name='name_layer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heat.material'),
        ),
    ]
