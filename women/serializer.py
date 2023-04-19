from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    class Meta:
        model = Women
        fields = ['title',
                  'content',
                  'time_create',
                  'time_update',
                  'is_published',
                  'cat_id']
        read_only_fields = ['time_create', 'time_update']

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance




