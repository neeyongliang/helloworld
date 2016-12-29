# Create your views here.
from django.shortcuts import render_to_response


def chapter_13(request):
    return render_to_response('chapter13/chapter.html')


def ex_1301(request):
    return render_to_response('chapter13/ex01.html')


def ex_1302(request):
    return render_to_response('chapter13/ex02.html')


def ex_1303(request):
    return render_to_response('chapter13/ex03.html')


def ex_1304(request):
    return render_to_response('chapter13/ex04.html')


def ex_1305(request):
    return render_to_response('chapter13/ex05.html')


def ex_1306(request):
    return render_to_response('chapter13/ex06.html')


def ex_1307(request):
    return render_to_response('chapter13/ex07.html')
