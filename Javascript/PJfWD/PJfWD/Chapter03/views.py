# Create your views here.
from django.shortcuts import render_to_response


def chapter_03(request):
    return render_to_response('chapter03/chapter.html')


def chapter_03_ex_01(request):
    return render_to_response('chapter03/ex01.html')