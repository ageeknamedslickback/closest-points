# Generated by Django 4.2.1 on 2023-05-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("points", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="closestpoint",
            name="closest_points",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
