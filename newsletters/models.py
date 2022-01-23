from django.db import models
from profiles.models import UserProfile


class Newsletters(models.Model):
    """ Model for site owners to post newsletters
     about the store"""

    class Meta:
        verbose_name_plural = 'newsletters'

    newsletters_title = models.CharField(max_length=254, blank=True, null=True,)
    newsletters_body = models.TextField(blank=True, null=True, default='')
    newsletters_by = models.CharField(max_length=254, default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newsletters_title
