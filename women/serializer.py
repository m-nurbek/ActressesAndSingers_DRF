from rest_framework import serializers
from django.db import models
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    # title = models.CharField(max_length=255)
    # content = models.CharField()
    # time_create = models.DateTimeField(read_only=True)
    # time_update = models.DateTimeField(read_only=True)
    # is_published = models.BooleanField(default=True)
    # cat_id = serializers.IntegerField()

    class Meta:
        model = Women
        fields = '__all__'
        read_only_fields = ['time_create', 'time_update']


# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title": Angelina Jolie", "content": Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
