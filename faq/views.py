from django.shortcuts import render

# Create your views here.

def about(request):
    """ A view to return the faq page """
    
    return render(request, 'faq/faq.html')