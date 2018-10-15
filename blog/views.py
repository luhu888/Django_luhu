import json

from django.shortcuts import render
from blog.models import BlogsPost
from django.http import HttpResponse
import requests


def blog_index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request, 'index.html', {'blog_list': blog_list})   # 返回index.html页面


def get_data(request, url):
    url = 'http://mock.xinheyun.com/mock/29/api/productPrice/getDetail'
    request = requests.get(url).text
    return HttpResponse(request)


def add_args(path):
    return path


def post(request):
    if request.method == 'POST':
        dic = {}
        if request.POST:
            path = request.POST.get('path', 0)
            if path:
                res = add_args(path)
                dic['path'] = res
                url = 'http://mock.xinheyun.com/'+path
                request = requests.get(url).text
                return HttpResponse(request)
            else:
                return HttpResponse('输入为空')
        else:
            return HttpResponse('方法错误')
    else:
        return HttpResponse('输入错误3')



