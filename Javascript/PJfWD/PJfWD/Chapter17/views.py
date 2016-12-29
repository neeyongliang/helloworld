from django.shortcuts import render_to_response


def chapter_17(request):
    return render_to_response('chapter17/chapter.html')


def ex_1701(request):
    return render_to_response('chapter17/ex01.html')


def ex_1702(request):
    return render_to_response('chapter17/ex02.html')


def ex_1703(request):
    return render_to_response('chapter17/ex03.html')


def ex_1704(request):
    return render_to_response('chapter17/ex04.html')


def ex_1705(request):
    return render_to_response('chapter17/ex05.html')
