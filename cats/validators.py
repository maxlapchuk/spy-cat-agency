import requests
from django.core.exceptions import ValidationError

API_VALIDATION_URL = "https://api.thecatapi.com/v1/breeds"


def validate_breed(value):
    valid_breeds = fetch_valid_breeds(API_VALIDATION_URL)
    if value not in valid_breeds:
        raise ValidationError(f"{value} is not a valid breed.")


def fetch_valid_breeds(validation_url):
    try:
        response = requests.get(validation_url)
        response.raise_for_status()
        return [breed["name"] for breed in response.json()]
    except requests.RequestException:
        return []


def validate_salary(value):
    if value < 0:
        raise ValidationError("Salary must be greater than zero.")
