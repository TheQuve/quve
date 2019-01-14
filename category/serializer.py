from rest_framework import serializers

from user.serializers import DetailUserSerializer
from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            'id',
            'contents'
        )


class CategoryMappingSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    user = DetailUserSerializer()

    class Meta:
        model = models.CategoryMapping
        fields = (
            'category',
            'user'
        )

