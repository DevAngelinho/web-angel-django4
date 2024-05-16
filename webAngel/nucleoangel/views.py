from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1>PROGRAMA EN CONSTRUCCION</h1><H2>La Web De Angel</h2>")

# Create your views here.
