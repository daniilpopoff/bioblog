from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

# Create your views here.

def sign_up(reqest):
    form = SignUpForm()
    if reqest.method == 'POST':
        form = SignUpForm(reqest.POST or None)
        if form.is_valid():
            user = form.save()
            login(reqest, redirect('home'))
    else:
        SignUpForm()
    return render(reqest,'sign_up.html', {'form' : form })