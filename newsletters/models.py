from django.db import models
from profiles.models import UserProfile


class Newsletters(models.Model):
    """ Model for site owners to post newsletters
     about the store"""

    newsletters_title = models.CharField(max_length=40, null=True, blank=True)
    newsletters_body = models.TextField(max_length=1000, null=True, blank=True)
    newsletters_by = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newsletters_title
