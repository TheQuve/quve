import json

# Create your views here.
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from category.models import Category, CategoryMapping
from category.serializer import CategorySerializer


class ListCategoryAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        queryset = Category.objects.all()

        serializer = CategorySerializer(
            queryset, many=True, context={'request': request})

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class CategoryAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, user_id):
        try:
            queryset = Category.objects.filter(
                categorymapping__user_id=user_id)

            serializer = CategorySerializer(
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

    def post(self, request, user_id):
        try:
            data = json.loads(request.body.decode('utf8'))
            category_ids = set(data.get('category_ids'))
            bulk_creator = []
            bulk_remover = []

            ids = set(CategoryMapping.objects.filter(
                user_id=user_id).values_list('category_id', flat=True))

            for _id in ids:
                if _id not in category_ids:
                    bulk_remover.append(_id)

            for category_id in category_ids:
                if category_id not in ids:
                    bulk_creator.append(CategoryMapping(
                        user_id=user_id,
                        category_id=category_id))

            CategoryMapping.objects.filter(
                user_id=user_id, category_id__in=bulk_remover).delete()

            CategoryMapping.objects.bulk_create(bulk_creator)

            queryset = Category.objects.filter(
                categorymapping__user_id=user_id)

            serializer = CategorySerializer(
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
