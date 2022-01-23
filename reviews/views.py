from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Reviews
from .forms import ReviewsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def reviews(request):
    """ A view to show all users reviews about our store"""
    reviews = Reviews.objects.all()

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }
    return render(request, template, context)


def view_reviews(request):
    """ A view displaying all reviews available """

    reviews = Reviews.objects.all()

    template = 'reviews/view_reviews.html'
    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_reviews(request):
    """ Add a reviews """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry only our customers can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'You have added your review successfully!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to add your review. please ensure the form is valid.')
    else:
        form = ReviewsForm()

    template = 'reviews/add_reviews.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ edit a review about the store"""
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry only our customers can do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Reviews, pk=review_id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been edit your review successfully!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewsForm(instance=review)
        messages.info(request, 'You will edit a your review')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete an existing review """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Reviews, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('reviews'))
