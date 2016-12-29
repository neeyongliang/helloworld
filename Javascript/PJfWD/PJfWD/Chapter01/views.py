# Create your views here.
from django.shortcuts import render_to_response


def chapter_01(request):
    return render_to_response('chapter01/chapter.html')


def chapter_01_ex_01(request):
    return render_to_response('chapter01/ex01.html')