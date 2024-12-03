from rest_framework import serializers

from .models import SpyCat
from .validators import validate_breed, validate_salary


class SpyCatSerializer(serializers.ModelSerializer):
    breed = serializers.CharField(
        validators=[validate_breed],
    )

    class Meta:
        model = SpyCat
        fields = ["id", "name", "years_of_experience", "breed", "salary"]
        read_only_fields = ["id"]


class SpyCatSalarySerializer(serializers.ModelSerializer):
    salary = serializers.IntegerField(
        validators=[validate_salary],
    )

    class Meta:
        model = SpyCat
        fields = ["salary"]
