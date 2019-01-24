from rest_framework import serializers

from answer.serializer import AnswerSerializer
from category.serializer import CategorySerializer, RegionSerializer
from user.serializers import DetailUserSerializer
from . import models
from answer.models import Answer


class ListQuestionSerializer(serializers.ModelSerializer):

    writer = DetailUserSerializer()
    category = CategorySerializer()

    class Meta:
        model = models.Question
        fields = (
            'id',
            'title',
            'writer',
            'category',
            'created_at',
            'updated_at',
            'region',
            'is_open',
            'limit',
            'user_class',
            'region',
            'point',
            'is_completed'
        )


class QuestionSerializer(serializers.ModelSerializer):

    writer = DetailUserSerializer()
    answer = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = models.Question
        fields = (
            'id',
            'title',
            'writer',
            'contents',
            'category',
            'created_at',
            'updated_at',
            'region',
            'user_class',
            'region',
            'is_open',
            'limit',
            'is_completed'
            'answer',
            'point'
        )

    def get_answer(self, obj):
        if 'request' in self.context:
            request = {'request': self.context['request']}
            queryset = Answer.objects.filter(question=obj)
            serializer = AnswerSerializer(
                queryset, many=True, context={'request': request})
            return serializer.data
        return []


class InputQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = (
            'title',
            'category',
            'contents',
            'point',
            'limit',
            'user_class',
            'region',
            'is_open',
            'is_completed'
        )
