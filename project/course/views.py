from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    return HttpResponse("<h1>This is project1<h1>")