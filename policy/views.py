from django.shortcuts import render

# Create your views here.

def policy(request):
    """ A view to return the policy page """
    
    return render(request, 'policy/policy.html')