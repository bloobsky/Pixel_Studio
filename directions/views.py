from django.shortcuts import render


def directions(request):
    """ A view to return the directionss page """

    return render(request, 'directions/directions.html')
