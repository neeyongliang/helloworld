from django.shortcuts import render_to_response


def chapter_20(request):
    return render_to_response('chapter20/chapter.html')


def ex_2001(request):
    return render_to_response('chapter20/ex01.html')


def ex_2002(request):
    return render_to_response('chapter20/ex02.html')


def ex_2003(request):
    return render_to_response('chapter20/ex03.html')
