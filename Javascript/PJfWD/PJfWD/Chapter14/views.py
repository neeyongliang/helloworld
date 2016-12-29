# Create your views here.
from django.shortcuts import render_to_response


def chapter_14(request):
    return render_to_response('chapter14/chapter.html')


def ex_1401(request):
    return render_to_response('chapter14/ex01.html')


def ex_1402(request):
    return render_to_response('chapter14/ex02.html')


def ex_1403(request):
    return render_to_response('chapter14/ex03.html')


def ex_1404(request):
    return render_to_response('chapter14/ex04.html')


def ex_1405(request):
    return render_to_response('chapter14/ex05.html')


def ex_1406(request):
    return render_to_response('chapter14/ex06.html')
