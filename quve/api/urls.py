from django.conf.urls import url

from quve.api.views.user import FacebookLogin

app_name = "api"

urlpatterns = [
    url(
        regex=r'^v1/login/facebook/$',
        view=FacebookLogin.as_view(),
        name='facebook_login'
    )
]
