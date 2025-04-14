#Quando for criar uma pagina você tem que levar esses três pontos em mente

# url - view - templete
from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilmes, Pesquisa, Editarperfil, Criarconta
from django.contrib.auth import views as auth_views #Como uma página de login é padrão no django já temos uma view pronta.

app_name = "filme"#nome da app que vai ser direcionada pra ulr principal do projeto

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"), #name serve para direncionar os link e identificar
    path('filmes/', Homefilmes.as_view(), name="homefilmes"), # sem os () por padrão o dj passa o request
    path('filmes/<int:pk>', Detalhesfilmes.as_view(), name="detalhesfilmes"),#pk = primery_key, pega os id do modelo filme
    path('pesquisa/', Pesquisa.as_view(), name='pesquisa'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Editarperfil.as_view(), name="editarperfil"),
    path('criar/', Criarconta.as_view(), name="criarconta"),
    path('mudarsenha/', auth_views.PasswordChangeView.as_view(template_name='editarperfil.html', success_url="reverse_lazy('filme:homefilmes)"), name='mudarsenha'),
]

