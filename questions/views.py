from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def questions(request):
    """ A view to render all the questions with
     thier related answers for all visitors"""

   

    template = 'questions/questions.html'
    context = {}

    return render(request, template, context)


def view_questions(request):
    """ A view to render all the questions with
     thier related answers for all visitors"""

   

    template = 'questions/view_questions.html'
    context = {}

    return render(request, template, context)


