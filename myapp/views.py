from django.shortcuts import render
from .forms import ContactForm
from .models import Contact


# Create your views here.

def home(request):
    return render(request,"index.html")

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
        
    }
    
    return render(request,"index.html",context)