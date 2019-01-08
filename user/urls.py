from django.conf.urls import url

from .views import FacebookLogin, RegistrationAPI, LoginAPI, UserAPI

app_name = "user"

urlpatterns = [
    url(
        regex=r'^login/facebook/$',
        view=FacebookLogin.as_view(),
        name='facebook_login'
    ),
    url("^register/$", RegistrationAPI.as_view()),
    url("^login/$", LoginAPI.as_view()),
    url("^info/$", UserAPI.as_view()),
]
