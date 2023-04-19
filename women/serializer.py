from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'
        read_only_fields = ['time_create', 'time_update']

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

