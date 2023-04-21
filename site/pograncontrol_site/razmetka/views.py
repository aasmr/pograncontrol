from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Case, CaseText
# Create your views here.

def login(request):
    return render(request, 'auth.html')

@login_required
def razmetka_page(request):
    return render(request, 'razmetka.html')