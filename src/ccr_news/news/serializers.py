from dataclasses import fields
from rest_framework import serializers
from .models import News, NewsTypes


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTypes
        fields = "__all__"