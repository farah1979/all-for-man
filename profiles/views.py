from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Please check that form is valid')

    else:
        form = UserProfileForm(request.POST, instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
            f'This is a past confirmation for order number {order_number}.'
            'A confirmation email was sent on the order date.'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)
