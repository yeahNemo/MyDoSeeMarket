from django.http import HttpResponse
from django.shortcuts import render

def hello(req):
    return HttpResponse("HelloWorld")

def runoob(req):
    context = {}
    context['hello'] = "我是内容！"
    return render(req,"runoob.html",context)