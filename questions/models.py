from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Model for logged in users to ask a question that needs an answer 
    from a cosmetic specialist
    """
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                            null=True, blank=True, related_name='user_question')
    title = models.CharField(max_length=300)
    detail = models.TextField(max_length=800, null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_answers(self):
        return self.answers.filter(parent=None)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='user_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True, related_name='answers')
    body = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_answers(self):
        return Answer.objects.filter(parent=self)
