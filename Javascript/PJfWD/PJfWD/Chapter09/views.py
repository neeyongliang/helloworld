from django.shortcuts import render_to_response


def chapter_09(request):
    return render_to_response('chapter09/chapter.html')


def ex_0901(request):
    return render_to_response('chapter09/ex01.html')


def ex_0902(request):
    return render_to_response('chapter09/ex02.html')


def ex_0903(request):
    return render_to_response('chapter09/ex03.html')


def ex_0904(request):
    return render_to_response('chapter09/ex04.html')
