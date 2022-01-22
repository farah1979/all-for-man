from django import forms
from .models import Newsletters


class NewslettersForm(forms.ModelForm):
    """ Create a form for onwner users to add newsletters """
    class Meta:
        model = Newsletters
        fields = ['newsletters_title',
                  'newsletters_body',
                  'newsletters_by', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
