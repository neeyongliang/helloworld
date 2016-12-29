# coding: utf-8
# __author__ = 'wikinee'
from django.shortcuts import render_to_response
from django.http import HttpResponse


def home(request):
    return render_to_response('welcome.html')

def tables(request):
    return render_to_response('elements/elements.html')

def framesetExample(request):
    return render_to_response('elements/framesetExample.html')

def topFrame(request):
    return render_to_response('elements/topFrame.htm')

def leftFrame(request):
    return render_to_response('elements/leftFrame.htm')

def rightFrame(request):
    return render_to_response('elements/rightFrame.html')

def redFrame(request):
    return render_to_response('elements/redFrame.htm')

def blueFrame(request):
    return render_to_response('elements/blueFrame.htm')

def form1(request):
    return render_to_response('elements/forms.html')

def richtext(request):
    return render_to_response('elements/richtext.html')

def blank(request):
    return render_to_response('elements/blank.html')
