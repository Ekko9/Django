from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world")


def test(request):
    context = {}
    context['hello'] = 'helloworld'
    return render(request, 'test.html', context)


# 循环字典
def dict1(request):
    dict1 = {'name': 'ekko', 'age': '26'}
    return render(request, 'dict1.html', {'people': dict1})


# 循环列表
def list1(request):
    list1 = [1, 2, 3]
    return render(request, 'list1.html', {'number': list1})


def index(request):
    return render(request, 'main.html')


def query(request):
    if request.is_ajax():
        print(request.body)
        print(request.POST)
        question = request.POST.get('question', '')
        return JsonResponse(
            {"isSuccess": True, 'msg': '测试成功，您提交的问题为' + question, 'status': 200, 'message': 'add event success'})
