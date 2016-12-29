# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse


def chapter_05(request):
    return render_to_response('chapter05/chapter.html')


def ex_0501(request):
    return render_to_response('chapter05/ex01.html')


def ex_0502(request):
    return render_to_response('chapter05/ex02.html')


def ex_0503(request):
    return render_to_response('chapter05/ex03.html')


def ex_0504(request):
    return render_to_response('chapter05/ex04.html')


def ex_0505(request):
    return render_to_response('chapter05/ex05.html')


def ex_0506(request):
    return render_to_response('chapter05/ex06.html')


def ex_0507(request):
    return render_to_response('chapter05/ex07.html')

