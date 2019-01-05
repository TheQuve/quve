from django.conf.urls import url

from .views import FacebookLogin

app_name = "user"

urlpatterns = [
    url(
        regex=r'^login/facebook/$',
        view=FacebookLogin.as_view(),
        name='facebook_login'
    )
]
