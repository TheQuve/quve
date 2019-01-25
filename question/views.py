# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from question.models import Question
from question.serializer import ListQuestionSerializer, QuestionSerializer, \
    InputQuestionSerializer


class ListQuestionAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        try:
            start = request.GET.get('start')
            limit = request.GET.get('limit')
            category = request.GET.get('category')
            point = request.GET.get('point')
            date = request.GET.get('date')

            queryset = Question.objects.all()

            if point:
                queryset = queryset.order_by('-point')

            if date:
                queryset = queryset.order_by('-created_at')

            if category:
                queryset = queryset.filter(category=category)

            if start and limit:
                start, limit = int(start), int(limit)
                queryset = queryset[start: start + limit]

            serializer = ListQuestionSerializer(
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


class QuestionAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, question_id):
        try:
            query = Question.objects.get(pk=question_id)

            serializer = QuestionSerializer(
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

    def put(self, request, question_id):
        try:
            user = request.user

            query = Question.objects.get(pk=question_id)

            if query.writer == user:
                serializer = InputQuestionSerializer(
                    query, data=request.data, partial=True)

                if serializer.is_valid():
                    point = request.data['point'] - query.point
                    user.point = user.point - point
                    user.save()
                    serializer.save(writer=user)
                    return Response(
                        data=serializer.data,
                        status=status.HTTP_200_OK
                    )
                return Response(
                    data=serializer.data,
                    status=status.HTTP_400_BAD_REQUEST
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
            query = Question.objects.get(pk=question_id)

            if query.writer == user:
                user.point = user.point + query.point
                user.save()
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


class InputQuestionAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        # try:
        request.data['category'] = int(request.data['category'])
        request.data['is_open'] = True
        request.data['is_completed'] = False
        request.data['point'] = int(request.data['point'])
        user = request.user
        serializer = InputQuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(writer=user)
            user.point = user.point - int(request.data['point'])
            user.save()
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        # except Exception as e:
        #     return Response(
        #         status=status.HTTP_400_BAD_REQUEST,
        #         data={'error': str(e)}
        #     )
