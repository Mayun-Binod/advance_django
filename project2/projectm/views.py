from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('This is Home page')


def learn_django(request):
    return HttpResponse('This is learn django page')


def learn_python(request):
    return HttpResponse('<h1>This is learn python page</h1>')


def learn_variable(request):
    a='<h1> Hello Variable </h1>'
    return HttpResponse(a)


def learn_format(request):
    b='Binod With Code'
    return HttpResponse(f"This is {b} ")

