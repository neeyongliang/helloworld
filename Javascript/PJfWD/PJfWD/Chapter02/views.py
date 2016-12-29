# Create your views here.
from django.shortcuts import render_to_response


def chapter_02(request):
    return render_to_response('chapter02/chapter.html')


def chapter_02_ex_01(request):
    return render_to_response('chapter02/ex01.html')


def chapter_02_ex_02(request):
    return render_to_response('chapter02/ex02.html')