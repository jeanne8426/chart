from django.shortcuts import render

def covid(request):
    return render(request, 'covid.html')

def covid2(request):
    return render(request, 'covid2.html')
