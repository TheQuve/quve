from django.conf.urls import url

from question.views import ListQuestionAPI, QuestionAPI, InputQuestionAPI

app_name = "question"

urlpatterns = [
    url("^question_list/$", ListQuestionAPI.as_view()),
    url("^(?P<question_id>[0-9]+)/$", QuestionAPI.as_view()),
    url("^input_question/$", InputQuestionAPI.as_view()),
]
