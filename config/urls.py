"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webrtc/', include('webrtc.urls', namespace='webrtc')),
    path('api/v1/user/', include('user.urls', namespace='user')),
    path('api/v1/answer/', include('answer.urls', namespace='answer')),
    path('api/v1/question/', include('question.urls', namespace='question')),
    path('api/v1/category/', include('category.urls', namespace='category')),
    path('api/auth', include('knox.urls')),
    url(
        regex='^rest-auth/',
        view=include('rest_auth.urls')
    ),
    url(
        regex='^rest-auth/registration/',
        view=include('rest_auth.registration.urls')
    ),
    url(
        regex=r"^accounts/",
        view=include("allauth.urls")
    )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path(
            'api/docs/', include_docs_urls(
                title='WebRTC',
                authentication_classes=[],
                permission_classes=[])
        )
    ]
