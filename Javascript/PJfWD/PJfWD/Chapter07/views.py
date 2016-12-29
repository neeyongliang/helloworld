# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse


def chapter_07(request):
    return render_to_response('chapter07/chapter.html')


def ex_0701(request):
    return render_to_response('chapter07/ex01.html')


def ex_0702(request):
    return render_to_response('chapter07/ex02.html')


def ex_0703(request):
    return render_to_response('chapter07/ex03.html')


def ex_0704(request):
    return render_to_response('chapter07/ex04.html')


def ex_0705(request):
    return render_to_response('chapter07/ex05.html')

