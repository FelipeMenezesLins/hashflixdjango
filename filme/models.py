from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser #O django por padrão já tem um modelo de usuario, nesse caso quando vc quer personalizar um usuario vc tem que dizer pro django que o modelo de usuario nao vai ser do padrao django


# Create your models here.

#criar um filme
#sub class vai receber no seu parametro seu modelo padrão é uma sub classe do models.Model
lista_categorias = (
    #Na tupla tem que armazenar duas informações uma que vai armazenar no banco de dados(armazenar.db, aparecer_pro_usuario)
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros")
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=lista_categorias)#No chafield vc vai passar dois parametros o máximo de caracteres que vai ocupar no seu bd, e passar a lista por meio do parametro choices
    vizualizacoes = models.IntegerField(default=0) #default um valor padrão
    data_criacao = models.DateTimeField(default=timezone.now)
    #Ela diz qual é o formato de string de um objeto nessa class, como você quer que ele seja exibido.
    def __str__(self):
        return self.titulo

#criar um usuario

#criar os espisodios
#fazendo uma referencia!

class Episodio(models.Model):
    #primeiro campo chave estrangeira pra fazer a referencia!!!!
    #Foreignkey("nome da tabela, releatade_name, server para add um campo especifico na tabela que vai ser acessado atraves do object. no html, on_delete = models.cascade serve para deletar todos epissdios relacionados ao filme deletado")
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)#ELE DIZ QUE ESSE ITEM FILME ESTÁ RELACIONADO COM A OUTRA TABELA, ALEM DISSO UM FILME PODE TER VARIOS EPISODIO MAIS VARIOS FILMES NÃO PODE FAZER REFERNCIA AO MESMO ESPISODIO. SE QUER QUE ISSO ACONTEÇA USA O models.ManyToManyField()
    titulo = models.CharField(max_length=100)
    video = models.URLField()#Fala que é um link
    def __str__(self):
        return self.titulo
    
class Usuario(AbstractUser):#voce normalmente iria colocar os campos do usuario mas o class abstractuser ela já vem com esses campos criados.
    filmes_vistos = models.ManyToManyField('Filme')