from django.shortcuts import render
from django.http import HttpResponse

#aqui, insiro todas as funções que chamaram as pages htmls
def index(request):
    return render(request, 'index.html')

def cursos(request):
    return render(request, 'cursos.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def acesso(request):
    return render(request, 'acesso.html')

def curso_adm(request):
    return render(request, 'curso_adm.html')

def curso_ads(request):
    return render(request, 'curso_ads.html')

def curso_bd(request):
    return render(request, 'curso_bd.html')

def curso_engenharia(request):
    return render(request, 'curso_engenharia.html')

def curso_gestao(request):
    return render(request, 'curso_gestao.html')

def curso_jogos(request):
    return render(request, 'curso_jogos.html')

def curso_producao(request):
    return render(request, 'curso_producao.html')

def curso_redes(request):
    return render(request, 'curso_redes.html')

def curso_sistemas(request):
    return render(request, 'curso_sistemas.html')