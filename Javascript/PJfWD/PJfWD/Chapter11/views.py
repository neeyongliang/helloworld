# Create your views here.
from django.shortcuts import render_to_response


def chapter_11(request):
    return render_to_response('chapter11/chapter.html')


def ex_1101(request):
    return render_to_response('chapter11/ex01.html')


def ex_1102(request):
    return render_to_response('chapter11/ex02.html')


def ex_1103(request):
    return render_to_response('chapter11/ex03.html')


def ex_1104(request):
    return render_to_response('chapter11/ex04.html')


def ex_1105(request):
    return render_to_response('chapter11/ex05.html')