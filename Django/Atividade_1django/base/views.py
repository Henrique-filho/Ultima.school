from django.shortcuts import render



def inicio (request):
    resposta = render(request, 'inicio.html')
    return resposta
