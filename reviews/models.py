from django.db import models
from profiles.models import UserProfile


class Reviews(models.Model):
    """A model for reviews"""
    class Meta:
        verbose_name_plural = 'reviews'

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True,
                             blank=True, related_name='user_review')
    review_name = models.CharField(max_length=245, null=True, blank=True)
    review_body = models.TextField(blank=True, null=True, default='')
    review_by = models.CharField(max_length=254, default='')
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_name
