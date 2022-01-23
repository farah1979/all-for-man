from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        exclude = (
            'user',
        )

        fields = [
            'review_name',
            'review_body',
            'review_by',
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'
