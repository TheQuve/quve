# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from question.models import Question
from .models import Answer
from .serializer import (
    ListAnswerSerializer, AnswerSerializer, InputAnswerSerializer)


class ListAnswerAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        try:
            start = request.GET.get('start')
            limit = request.GET.get('limit')
            queryset = Question.objects.filter(is_completed=True)

            if start and limit:
                start, limit = int(start), int(limit)
                queryset = queryset[start: start + limit]

            serializer = ListAnswerSerializer(
                queryset, many=True, context={'request': request})

            return Response(
                status=status.HTTP_200_OK,
                data={
                    'data': serializer.data
                }
            )
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error': str(e)}
            )


class AnswerAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, answer_id):
        try:
            query = Answer.objects.get(pk=answer_id)

            serializer = AnswerSerializer(
                query, context={'request': request})
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error': str(e)}
            )

    def put(self, request, answer_id):
        try:
            user = request.user

            query = Answer.objects.get(pk=answer_id)

            if query.writer == user:
                serializer = InputAnswerSerializer(
                    query, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save(writer=user)
                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK
                )

            else:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error': str(e)}
            )

    def delete(self, request, question_id):
        try:
            user = request.user
            query = Answer.objects.get(pk=question_id)

            if query.writer == user:
                query.delete()
                return Response(
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error': str(e)}
            )


class InputAnswerAPI(APIView):
    def post(self, request):
        try:
            user = request.user
            serializer = InputAnswerSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(writer=user)

                return Response(
                    status=status.HTTP_200_OK,
                    data=serializer.data
                )
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error': str(e)}
            )

# Create your views here.
