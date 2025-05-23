from rest_framework import serializers
from .models import Person
import re


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    def validate_phone_number(self, value):
        pattern = r'^\d{3}-\d{3}-\d{4}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Invalid phone number format. It should be in the format 123-456-7890.")
        return value
