from rest_framework import serializers

from main.models import SomeString


class SomeStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeString
        fields = (
            'string',
        )
