#coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse

def api(request):
    return HttpResponse("API LIST");


def testforget(request):
    return HttpResponse("不知道怎么设置heder中Content-Length 字段,test for get method!");
