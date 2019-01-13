from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            'id',
            'contents'
        )


class CategoryMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CategoryMapping
        fields = (
            'category',
            'user'
        )

