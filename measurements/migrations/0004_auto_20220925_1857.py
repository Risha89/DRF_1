# Generated by Django 3.1.2 on 2022-09-25 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0003_auto_20220925_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='measurements',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurements.measurement'),
        ),
    ]
