from django.db import models

from .validators import validate_breed, validate_salary


class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    breed = models.CharField(
        max_length=100,
        validators=[validate_breed],
    )
    salary = models.IntegerField(
        validators=[validate_salary],
    )
