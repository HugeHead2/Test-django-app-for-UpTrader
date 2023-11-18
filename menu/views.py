from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'menu/index.html')


def categoreis(request):
    return render(request, 'menu/categories.html')


def first_category(request):
    return render(request, 'menu/FirstCategory.html')


def second_category(request):
    return render(request, 'menu/SecondCategory.html')


def about(request):
    return render(request, 'menu/About.html')
