from django.contrib import admin
from .models import Reviews

class ReviewsAdmin(admin.ModelAdmin):
    """ for register reviews model in admin panel"""
    list_display = (
        'user',
        'review_name',
        'review_body',
        'review_by',
        'review_date',
    )

    ordering = ('review_name',)

admin.site.register(Reviews, ReviewsAdmin)
