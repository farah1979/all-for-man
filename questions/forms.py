from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Question, Answer
from django.contrib.auth.models import User


class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = (
            'user',
        )

        fields = ['title', 'detail']
        widgets = {
            'title': forms.TextInput(attrs={
                'autofocus': True,
                'placeholder': 'Question Title',
            })
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 col-12'

class NewAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'autofocus': True,
                'placeholder': 'Answer details',
                'rows': 6,
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 col-12'