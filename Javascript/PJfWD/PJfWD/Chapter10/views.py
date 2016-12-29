# Create your views here.
from django.shortcuts import render_to_response


def chapter_10(request):
    return render_to_response('chapter10/chapter.html')


def ex_1001(request):
    return render_to_response('chapter10/ex01.html')


def ex_1002(request):
    return render_to_response('chapter10/ex02.html')


def ex_1003(request):
    return render_to_response('chapter10/ex03.html')
