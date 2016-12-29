# Create your views here.
from django.shortcuts import render_to_response


def chapter_12(request):
    return render_to_response('chapter12/chapter.html')


def ex_1201(request):
    return render_to_response('chapter12/ex01.html')


def ex_1202(request):
    return render_to_response('chapter12/ex02.html')


def ex_1203(request):
    return render_to_response('chapter12/ex03.html')


def ex_1204(request):
    return render_to_response('chapter12/ex04.html')


def ex_1205(request):
    return render_to_response('chapter12/ex05.html')
