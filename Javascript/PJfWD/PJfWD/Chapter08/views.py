# Create your views here.
from django.shortcuts import render_to_response


def chapter_08(request):
    return render_to_response('chapter08/chapter.html')


def ex_0801(request):
    return render_to_response('chapter08/ex01.html')


def ex_0802(request):
    return render_to_response('chapter08/ex02.html')


def ex_0803(request):
    return render_to_response('chapter08/ex03.html')


def ex_0804(request):
    return render_to_response('chapter08/ex04.html')


def ex_0805(request):
    return render_to_response('chapter08/ex05.html')


def ex_0806(request):
    return render_to_response('chapter08/ex06.html')
