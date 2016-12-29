# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse


def chapter_06(request):
    return render_to_response('chapter06/chapter.html')


def ex_0601(request):
    return render_to_response('chapter06/ex01.html')


def ex_0602(request):
    return render_to_response('chapter06/ex02.html')


def ex_0603(request):
    return render_to_response('chapter06/ex03.html')


def ex_0604(request):
    return render_to_response('chapter06/ex04.html')
