from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Question, Answer
from .forms import NewQuestionForm, NewAnswerForm



def questions(request):
    """ A view to render all the questions with
     thier related answers for all visitors"""
    questions = Question.objects.all().order_by('-created_at')

    template = 'questions/questions.html'
    context = {
       'questions': questions,
    }

    return render(request, template, context)

def view_questions(request, question_id):

    answer_form = NewAnswerForm()

    if request.method == 'POST':
        try:
            answer_form = NewAnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.user = request.user
                answer.question = Question(pk=question_id)
                answer.save()
                messages.success(request, 'Our experts answer!')
                return redirect(reverse('questions'))
        except Exception as e:
            messages.error(request, 'Sorry check your form')

    question = Question.objects.get(pk=question_id)

    template = 'questions/view_questions.html'
    context = {
        'question': question,
        'answer_form': answer_form,
    }

    return render(request, template, context)

@login_required
def add_questions(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry only our customers can do that.')
        return redirect(reverse('questions'))
    form = NewQuestionForm()

    if request.method == 'POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.user = request.user
                question.save()
                messages.success(request, 'Your question has been saved successfully. Our experts will respond \
                                to you as soon as possible')

        except Exception as e:
                print(e)
                raise

    template = 'questions/add_questions.html'
    context = {
        'form': form,
    }
    return render(request, template, context)