from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse("<h1>Hola mundo</h1>.")

def inventario(request):
	lista = models.Producto.objects.all()
	return render(request, "inventario.html", {'lista':lista})
