from django.conf.urls import url

from category.views import ListCategoryAPI, CategoryAPI

app_name = "category"

urlpatterns = [
    url("^category_list/$", ListCategoryAPI.as_view()),
    url("^(?P<user_id>[0-9]+)/$", CategoryAPI.as_view()),
]
