from django.shortcuts import render
from .models import Question
from products.models import Category

# Create your views here.

def faq(request):
    """ A view to return the faq page """
    
    
    question = Question.objects.all()
    categories = Category.objects.all()
    webdev = Question.objects.filter(category='1')
    context = {
            'question': question,
        }
    return render(request, 'faq/faq.html', context)