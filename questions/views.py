from django.shortcuts import render, redirect, reverse, get_object_or_404
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
                return redirect('view_questions', question_id=question_id)
            else:
                messages.error(request, 'Please ckeck if the form is valid')

        except Exception as e:
            print(e)
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
                question.author = request.user
                question.save()
                messages.success(request, 'Your question has been saved successfully. Our experts will respond \
                                to you as soon as possible')
            return redirect(reverse('questions'))

        except Exception as e:
            messages.error(request, 'No question added, Please check the form is valid!')

    template = 'questions/add_questions.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def edit_question(request, question_id):
    """ edit a question in the store"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('questions'))

    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = NewQuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been edit your question successfully!')
            return redirect(reverse('questions'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = NewQuestionForm(instance=question)
        messages.info(request, f'You are editing {question.title}')

    template = 'questions/edit-question.html'
    context = {
        'form': form,
        'question': question,
    }

    return render(request, template, context)

@login_required
def delete_question(request, question_id):
    """ Delete an existing question """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('questions'))

    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    messages.success(request, 'Question deleted!')
    return redirect(reverse('questions'))
