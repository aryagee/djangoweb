from django.http import HttpResponse
from django.shortcuts import render
def home(req):
    return render(req, 'index.html')
    # return HttpResponse('<h1>Hello world</h1>')

def results(request):
    name = request.GET.get('user_name')
    age = request.GET.get('age')
    message = f'hi,{name} you are {age} years old'
    return render(request, 'results.html',{'key':message})