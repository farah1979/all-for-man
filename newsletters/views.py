from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Newsletters
from .forms import NewslettersForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def newsletters(request):
    """ A view render all newsletters from superusers to page"""
    newsletters = Newsletters.objects.all()

    template = 'newsletters/newsletters.html'
    context = {
        'newsletters': newsletters,
    }

    return render(request, template, context)


@login_required
def add_newsletter(request):
    """ Add a newsletter about the store and products"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = NewslettersForm(request.POST, request.FILES)
        if form.is_valid():
            newsletter = form.save()
            messages.success(request, 'You have added your newsletter successfully!')
            return redirect(reverse('newsletters'))
        else:
            messages.error(request, 'Failed to add newsletter. please ensure the form is valid.')
    else:
        form = NewslettersForm()

    template = 'newsletters/add_newsletter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_newsletter(request, newsletter_id):
    """ edit a newsletter about the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    newsletter = get_object_or_404(Newsletters, pk=newsletter_id)
    if request.method == 'POST':
        form = NewslettersForm(request.POST, request.FILES, instance=newsletter)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been edit the newsletter successfully!')
            return redirect(reverse('newsletters'))
        else:
            messages.error(request, 'Failed to update newsletter. Please ensure the form is valid.')
    else:
        form = NewslettersForm(instance=newsletter)
        messages.info(request, 'You will edit a newsletter')

    template = 'newsletters/edit_newsletter.html'
    context = {
        'form': form,
        'newsletter': newsletter,
    }

    return render(request, template, context)


@login_required
def delete_newsletter(request, newsletter_id):
    """ Delete an existing newsletter """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    newsletter = get_object_or_404(Newsletters, pk=newsletter_id)
    newsletter.delete()
    messages.success(request, 'Newsletter deleted!')
    return redirect(reverse('newsletters'))
