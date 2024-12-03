from django.core.exceptions import ValidationError
from django.db import models

from cats.models import SpyCat


class Mission(models.Model):
    spy_cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE, null=True, blank=True)
    is_completed = models.BooleanField(default=False)


class Target(models.Model):
    mission = models.ForeignKey(
        Mission, related_name="targets", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            targets_count = self.mission.targets.count()
            if targets_count >= 3:
                raise ValidationError("A mission can have a maximum of 3 targets")
        super().save(*args, **kwargs)
