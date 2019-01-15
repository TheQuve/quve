from django.conf.urls import url

from .views import ListAnswerAPI, AnswerAPI, InputAnswerAPI
from question.views import QuestionAPI

app_name = "answer"

urlpatterns = [
    url("^answer_list/$", ListAnswerAPI.as_view()),
    url("^read/(?P<answer_id>[0-9]+)/$", AnswerAPI.as_view()),
    url("^(?P<question_id>[0-9]+)/$", QuestionAPI.as_view()),
    url("^input_answer/$", InputAnswerAPI.as_view()),
]
