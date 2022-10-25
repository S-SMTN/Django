from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import *

menu = [{'title': "Розділ 1", 'url_name': 'section-1'},
        {'title': "Розділ 2", 'url_name': 'section-2'},
        {'title': "Розділ 3", 'url_name': 'section-3'},
        {'title': "Увійти", 'url_name': 'login'},
        {'title': "Зареєструватися", 'url_name': 'register'},
]

# Create your views here.
def index(request):
    data = ["JOPA!", "Pipa"]
    variable = {'variable': data}
    return render(request, 'initialization\index.html', variable)

def initialization(request, id):
    names = list(request.GET)
    values = [request.GET[name] for name in names]
    couples = []
    for i in range(0, len(names)):
        couples.append(f"{names[i]}: {values[i]}")
    couples = ", ".join(couples)
    return HttpResponse(f"Страница приложения initialization, id = {id}<p>Переменные: {couples}.</p>")

def archive(request, year):
    if int(year) > 2028:
        raise Http404()
    if int(year) < 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f"Страница приложения initialization, архив, год = {year}")

def page404(request, exception):
    return HttpResponseNotFound("А что ты хотел увидеть?")