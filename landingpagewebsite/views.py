from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = "<h3>hello</h3>"
    text = "NEW TEXT"

    return render(request, './index.html', {
        'a': a,
        'text': text
    })

def testi_page(request):
    a = "Hello World"

    return render(request, './testi.html', {
        'a': a
    })