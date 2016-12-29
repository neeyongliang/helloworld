from django.shortcuts import render_to_response


def chapter_15(request):
    return render_to_response('chapter15/chapter.html')


def ex_1501(request):
    return render_to_response('chapter15/ex01.html')


def ex_1502(request):
    return render_to_response('chapter15/ex02.html')


def ex_1503(request):
    return render_to_response('chapter15/ex03.html')


def ex_1504(request):
    return render_to_response('chapter15/ex04.html')
