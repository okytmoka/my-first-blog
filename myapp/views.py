from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import item

# Create your views here.
def index(request):
    html = "<h1>myappのウェルカムページです</h1>"
    return HttpResponse(html)

def foo(request):
    html = "<h1>fooが指定されたときのページです</h2>"
    return HttpResponse(html)

def hello(request):
    context = {
        'datetime':datetime.now(),
        'message':'Templateを使ってみよう'
    }
    return render(request,'index.html',context)

def show_item(request,item_code):
    Item = item.objects.get(code=item_code)
    context = {'item':Item,}
    return render(request,'item.html',context)
