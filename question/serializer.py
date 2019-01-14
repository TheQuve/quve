from rest_framework import serializers

from user.serializers import DetailUserSerializer
from . import models


class ListQuestionSerializer(serializers.ModelSerializer):

    writer = DetailUserSerializer()

    class Meta:
        model = models.Question
        fields = (
            'id',
            'title',
            'writer',
            'created_at',
            'updated_at',
            'is_completed'
        )


class QuestionSerializer(serializers.ModelSerializer):

    writer = DetailUserSerializer()

    class Meta:
        model = models.Question
        fields = '__all__'


class InputQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = (
            'title',
            'contents',
            'is_completed'
        )
