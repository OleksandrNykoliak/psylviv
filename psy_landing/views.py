from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')


def bozhenasadova(request):
    return render(request, 'personal/bozhenasadova.html')
