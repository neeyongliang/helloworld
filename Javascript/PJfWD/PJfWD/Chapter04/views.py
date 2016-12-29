# Create your views here.
from django.shortcuts import render_to_response


def chapter_04(request):
    return render_to_response('chapter04/chapter.html')