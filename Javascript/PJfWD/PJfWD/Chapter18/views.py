from django.shortcuts import render_to_response


def chapter_18(request):
    return render_to_response('chapter18/chapter.html')


def ex_1801(request):
    return render_to_response('chapter18/ex01.html')


def ex_1802(request):
    return render_to_response('chapter18/ex02.html')


def ex_1803(request):
    return render_to_response('chapter18/ex03.html')


def ex_1804(request):
    return render_to_response('chapter18/ex04.html')
