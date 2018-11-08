from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'contactForm': form})
