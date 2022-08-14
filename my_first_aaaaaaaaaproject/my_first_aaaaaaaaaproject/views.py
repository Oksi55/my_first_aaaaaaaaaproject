from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 5 + 6
    return render(request, '1.html', {'gretting': a})



def home(request):
    return HttpResponse('This is my home')