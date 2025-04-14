from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin
# Register your models here.
#diz onde seus arquivos vão estar no admin
#ISSO SÓ EXISTE PQ NOS QUEREMOS QUE ESSE CAMPO PERSONALIZADO filmes_vistos APAREÇA NO ADMIN
campos = list(UserAdmin.fieldsets)
campos.append(
    ("nome_da_seção", {'fields': ('filmes_vistos',)})
    #uma tupla dentro dela tem o nome da seção do usuario, e o segundo item é um dicionario com a chave com uma outra tupla onde passa os nomes
)
UserAdmin.fieldsets = tuple(campos)

#exemplo essa função fieldsets ela vai transforma um useradmin numa lista, pra isso temos aque add na nossa lista usando sua estrutura do fieldsets que é:
# [
# ("nome_da_seção", {'fields': ('primeiro nome', "Ultimo nome")})
# ]

admin.site.register(Filme)#registra seu modelo no campo admin
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)#Esse useradmin é uma class responsável pela gestão de usuarios sobre como vc pode saber quem é o usuario se ele tiver com tres abas abertas vc saber que é o mesmo usuario. E pra usar essa class vc tem que importa ela.
#Se vc está se pergutando o pq n foi add oq vc fez no seu usuario, é que ele ta mostrando o useradmin e n os campos do seu modelo de usuario, pra fazer isso voce ter que fazer uma lista dos campos que vc quer que apareça