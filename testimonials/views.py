from django.shortcuts import render


def testimonials(request):
    """ A view to return the testimonials page """

    return render(request, 'testimonials/testimonials.html')
