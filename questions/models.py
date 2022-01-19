from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Model for logged in users to ask a question that needs an answer 
    from a cosmetic specialist
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True)
    question_title = models.CharField(max_length=300)
    question_by = models.CharField(max_length=25, default='')
    detail = models.TextField(max_length=800, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, blank=False, null=True)
    detail = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail


# Comment
class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    created = models.DateTimeField(auto_now_add=True)


# UpVotes
class UpVote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_user')


# downVotes
class DownVote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_user')
