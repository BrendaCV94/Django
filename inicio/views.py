from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    
    return render(request, 'inicio/inicio.html')
#     return HttpResponse('<h1>Hola Soy la vista de inicio</h1>')
# # Create your views here.
