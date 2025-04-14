#cria todas as variaveis que as paginas templates vai ter acessos
#Depois para conectar ele aos seus templates vá em settings depois templates lá vai ter o cotext_process e vc vai add suas funções lá

from .models import Filme #importa nosso db

def lista_filmes_recentes(request):
    #uma lista de itens lembra
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:10]#serve para pegar todos os objetos dentro do db, order_by ordena por ordem decresente quando coloca o -
    return {"lista_filmes_recentes": lista_filmes}#retorna um context, que seria um dicionario onde tem uma chave na qual se vai usar pra mostrar no seu html, e o valor do dicionario.

def filmes_populares(request):
    lista_filmes_populares = Filme.objects.all().order_by('-vizualizacoes')[0:10]
    return {"filmes_populares": lista_filmes_populares}

def filmes_destaques(requets):
    lista_filmes_destaques = Filme.objects.all().order_by('-data_criacao')
    if lista_filmes_destaques:
        destaque_filme = lista_filmes_destaques[0]
        return{"lista_destaque": destaque_filme}
    else:
        destaque_filme = None
        return{"lista_destaque": destaque_filme}

    