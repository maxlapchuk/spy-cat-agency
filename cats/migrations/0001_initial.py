# Generated by Django 5.1.3 on 2024-12-03 17:49

import cats.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SpyCat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("years_of_experience", models.IntegerField(max_length=2)),
                (
                    "breed",
                    models.CharField(
                        max_length=100, validators=[cats.validators.validate_breed]
                    ),
                ),
                ("salary", models.IntegerField()),
            ],
        ),
    ]
