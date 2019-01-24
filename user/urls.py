from django.conf.urls import url

from .views import FacebookLogin, RegistrationAPI, LoginAPI, UserAPI, \
    UserClassAPI

app_name = "user"

urlpatterns = [
    url(
        regex=r'^login/facebook/$',
        view=FacebookLogin.as_view(),
        name='facebook_login'
    ),
    url("^register/$", RegistrationAPI.as_view()),
    url("^login/$", LoginAPI.as_view()),
    # url("^info/$", UserAPI.as_view()),
    url("^user_class/$", UserClassAPI.as_view()),
    url("^(?P<user_id>[0-9]+)/$", UserAPI.as_view()),
]
