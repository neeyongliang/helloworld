from django.shortcuts import render_to_response


def chapter_16(request):
    return render_to_response('chapter16/chapter.html')


def ex_1601(request):
    return render_to_response('chapter16/ex01.html')


def ex_1602(request):
    return render_to_response('chapter16/ex02.html')


def ex_1603(request):
    return render_to_response('chapter16/ex03.html')


def ex_1604(request):
    return render_to_response('chapter16/ex04.html')


def ex_1605(request):
    return render_to_response('chapter16/ex05.html')
