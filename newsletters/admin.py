from django.contrib import admin
from newsletters.models import Newsletters


class NewslettersAdmin(admin.ModelAdmin):
    """ to register newsletters model in admin pannel """

    list_display = (
        'newsletters_title',
        'newsletters_body',
        'newsletters_by',
        'date',
    )
    ordering = ('date',)


admin.site.register(Newsletters, NewslettersAdmin)
