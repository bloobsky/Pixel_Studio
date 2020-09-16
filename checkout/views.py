from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in you cart !!!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HRvIHH91IUrTXtUHsAKFlicNZSl8SekzV2yYsceuKZGEtSVdD8GQfZ17LYG6NAynbj7oAhSFJoNNDyhzgxUUXvh00LIDPgwjH',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
