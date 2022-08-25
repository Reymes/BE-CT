from rest_framework import serializers
from .models import AntDoc


class AntDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntDoc
        fields = ["document","id"]
