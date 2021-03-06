from django.shortcuts import render
from django.http import HttpResponse
from T.models import *
from datetime import datetime

import json

# Llamar Templates
def ruta(request):
  proyecto = obtener_proyecto()
  rutas = obtener_rutas(proyecto.codPyto)
  return render(request, 'rutas.html', {'proyecto': proyecto, 'rutas': rutas})

def reconocimiento(request):
  return render(request, 'reconocimiento.html')


# Realizar consultas
def get_empleado(): # Funcion de prueba, eliminarlo despues
  empleado = Empleado.objects.get(dni = '77382771')
  return empleado

def obtener_proyecto():
  proyecto = Proyecto.objects.get(codPyto = 2)
  return proyecto

def obtener_rutas(cod):
  rutas = Ruta.objects.filter(codPyto=cod)
  return rutas

def obtener_tramos():
  tramos = Tramo.objects.all()
  return tramos