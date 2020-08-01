from rest_framework import serializers
from .models import hackers

class hackersSerializer(serializers.ModelSerializer):
    class Meta:
        model = hackers
        fields = '__all__'