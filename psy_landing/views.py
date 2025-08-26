from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def bozhenasadova(request):
    return render(request, 'personal/bozhenasadova.html')
