#criar nossos formularios personalizados
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario
from django import forms #serve para add um campo de formulario

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()# se vc n passa nada entre os parenteses esse campo ele é obrigatório. opcional é required = False
    #Nesse usercreationform vc precisa dizer pra ele dentro dessa class voce tem que definir uma outra class chamada meta:

    class Meta:#diz pra ele quem é o modelo que ele tem que utilizar como referencia.
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')#fields é uma tupla onde vai exebir os campos dos formularios, que tem esse nome padrão da class usercreationform

class FormDaHomePage(forms.Form):#estmaos criando um formulário padrão do django então não precisamos da usercreationform.
    email = forms.EmailField(label=False)