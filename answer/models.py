from django.db import models

from question.models import Question
from user.models import TimeStampedModel, User


class Answer(TimeStampedModel):
    contents = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title
