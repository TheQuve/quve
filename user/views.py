from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import UserClass, User
from .serializers import (
    CreateUserSerializer,
    UserSerializer,
    LoginUserSerializer,
    UserClassSerializer)
from knox.models import AuthToken

from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter
)
from rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user),
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user),
            }
        )


class UserAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, user_id):
        try:
            query = User.objects.get(pk=user_id)

            if query == request.user:

                serializer = UserSerializer(
                    query, context={'request': request})
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'data': serializer.data
                    }
                )
            else:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'error': str(e)
                }
            )

    def put(self, request, user_id):
        try:
            query = User.objects.get(pk=user_id)

            if query == request.user:
                serializer = UserSerializer(
                    query, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer = UserSerializer(
                        query, context={'request': request})
                    return Response(
                        status=status.HTTP_200_OK,
                        data={
                            'data': serializer.data
                        }
                    )
                return Response(
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'error': str(e)
                }
            )


class UserClassAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        queryset = UserClass.objects.all()
        serializer = UserClassSerializer(
            queryset, many=True, context={'request': request})
        return Response(
            status=status.HTTP_200_OK,
            data={
                'data': serializer.data
            }
        )
