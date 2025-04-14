from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView #uma class que verifica o form
from .forms import CriarContaForm, FormDaHomePage
from django.contrib.auth.mixins import LoginRequiredMixin #Importa uma class que é responsavel para bloquear as páginas e permitir o acesso só pra quem estiver logado no site, detalhe importante é que essa class tem que ser passada como o 1 parametro exemplo: class Homepage(LoginRequiredMixin, TemplateView)
# Create your views here.
# EXPLICAÇÃO DO REQUEST

# Quando você entra em um site, você faz uma requisição, a qual pode ser duas formas, get e post, quando você entra em um site você tá fazendo uma requisição do tipo get, uma requisição do tipo post é quando você preenche um formulário e envia ele.

#E ele é obrigatório porque ele tá dizendo pra essa view se ele é uma requisição do tipo get ou post

# def homepage(request):
#     return render(request, "homepage.html")# o render por padrao recebe o request e  o arquivo template.

class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormDaHomePage

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('flime:criarconta')

    def get(self, request, *args, **kwargs): # nosso user fica dentro do request então vai ser request.user.is_authenticated
        if request.user.is_authenticated : #verifica se o usuario está logado
            return redirect('filme:homefilmes')#Não usaremos o render pq ele n iria funcionar bem com isso
        else:
        #Caso o usuario não estiver logado redireciona para url final que é a minha homepage
            return super().get(request, *args, **kwargs)

# def homefilmes(request):
#     context = {}
#     listas_filmes = Filme.objects.all() #pega todos os objetos dentro da sua class .all()
#     context['listas_filmes'] = listas_filmes
#     return render(request, "homefilmes.html", context)

#você passar as informações do banco de dados para a parte front, é um context q é básicamente um dicionario no python

#TRANSFORMANDO NOSSA FUNÇÃO EM UMA CLASS BASED VÍDEO 21

# A lista view pede duas variavel o nome do template e o seu modelo.

class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme #object_list -> todos os itens do modelo
    #Ele oferece o context e retorna com o nome de chave de object_list
   
#Criando viwes pro nossos filmes
#Como não é um template nois vamos exibir os detlhes desse item com o dateils view

class Detalhesfilmes(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilmes.html"
    model = Filme
    #  retorna com o nome object -> 1 item do modelo
    def get(self, request, *args, **kwargs): #a gente vai retornar uma super porque estamos editando uma função de class que já existe
        #contabilizou a vizualização
        filme = self.get_object()
        filme.vizualizacoes += 1
        filme.save() # salvou no banco de dados
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) #redireciona o usuario pra url final



    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria= self.get_object().categoria)[0:3]

        context['filmes_relacionados'] = filmes_relacionados

        return context
    
class Pesquisa(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self): #função pronta serve para pegar os parametros passado na url!
        termo_pesquisa = self.request.GET.get('query') #qual a pesquisa que ele passou no input, self.request.GET eu quero que ele execute quando ele usar essa requisição method get. o GET é o tipo da requisição e o .get é oq eu quero pegar como parametro
        #E dentro do get('nome do input') vai passar o name do seu input
        if termo_pesquisa: # Voce pode colocar no local de Filme self.model  pq ele vai estar se referindo ao modelo da nossa class model = Filme
            object_list = Filme.objects.filter(titulo__icontains = termo_pesquisa)#aqui eu to passando um filtro pro meu object_list, o parametro icontains serve pra dizer cotem a nossa pesquisa. nesse caso é o titulo que a gente passou.
            return object_list
        else:
            return None

class Editarperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']# a Updateview pede o fields e o modelo, esse first last, são tudo do nosso abstract user da class padrão, então por isso que os nomes estão assim desse jeito
    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta (FormView):
    template_name = 'criar.html'
    form_class = CriarContaForm

    #quando voce criar um form view vc tem que tratar ou editar 2 def

    def form_valid(self, form):#verifica se o formulario é valido
        form.save()#salva o usuario e add um item no banco de dados
        return super().form_valid(form)
    

    def get_success_url(self):#Te direciona caso a conta for aprovada ela te direciona através de um link. ELA ESPERA UM URL COMO RESPOSTA por isso n usamos o redirect.
        return reverse('filme:login')
