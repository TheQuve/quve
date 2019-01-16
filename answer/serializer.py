from rest_framework import serializers

from category.serializer import CategorySerializer
from user.serializers import DetailUserSerializer
from question.models import Question
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    writer = DetailUserSerializer()

    class Meta:
        model = Answer
        fields = (
            'id',
            'contents',
            'is_selected',
            'writer'
        )


class ListAnswerSerializer(serializers.ModelSerializer):

    writer = DetailUserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'writer',
            'category',
            'created_at',
            'updated_at',
            'is_completed'
        )


class InputAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'contents',
            'question'
        )