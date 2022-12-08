from django.shortcuts import render

def Home(request):
  return render(request,'home.html')

def QuienesSomos(request):
  return render(request, 'quienesSomos.html')

def Contacto(request):
  return render(request, 'contacto.html')