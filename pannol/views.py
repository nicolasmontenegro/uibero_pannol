from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
    return HttpResponse("<h1>Hola mundo</h1>.")

def inventario(request):
	valores = {
		"titulo": "Hola mundo",
		"subtitulo": "inventario",
		"lista": None,
	}
	lista = models.Producto.objects.all()
	if len(lista):
		valores["lista"]=lista 
	return render(request, "inventario.html", valores)

def about():
	pass