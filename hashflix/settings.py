"""
Django settings for hashflix project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!ng=3inhx0&6)-%(3qsun-3x78j3v4^bybxhue+2rhx)bs@p03'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["https://hashflixdjango-production-74f7.up.railway.app"]#link do seu site!



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filme',
    'crispy_forms',
    'crispy_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", #Depois do django.securuty processo de DEPLOY
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hashflix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'filme.context.lista_filmes_recentes',
                'filme.context.filmes_populares',
                'filme.context.filmes_destaques',
            ],
        },
    },
]

WSGI_APPLICATION = 'hashflix.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',#AQUI É IMPORTANTE PQ SÓ TEMOS NOSSO BANCO DE DADOS LOCAL, TEMOS QUE FAZER O BANCO DE DADOS ONLINE PARA O DEPLOY DO NOSSO SITE ONDE ELE VAI PEGAR AS INFORMAÇÕES DO NOSSO BANCO DE DADOS LOCAL, NO PROCFILE ELE É GERENCIADO PELO GUNINCORN
        #PRA FAZER ISSO TEMOS QUE INSTALAR MAIS UMA BIBLIOTECA
        #pip install dj-database-url
        # o db online precisa de uma biblioteca tbm
        #pip install psycopg2
    }
}
#Importamos a biblioteca que intalamos
import dj_database_url
import os #pertmite que trabalha com váriaveis de ambiente que não tem no seu cod

DATABASE_URL = os.getenv("URL_DO_BANCO_DE_DADOS")#ele só funciona se vc tiver rodando o cod lá no servidor!

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800)#Serve para cortar uma conexão do banco de dados, é basicamente o tempo pra cortar
        #db tem um limite máximo pra pegar conexões e caso vc n corte vc estara sobrecarregando o seu db
    }

#DEPOIS DE COFING O DB, VAMOS DÁ DEPLOY, 
#primeiro git init 
# git add . adiciona tds o seus arquivos
#git -m "first commit" serve para atualizar os arquivos no github
#pra alterações e para atualizar vc vai fazer sempre esses comandos, git add ., git -m"first commit" e  git push -u origin main
#git config --global user.email "felipemenezesmk22@gmail.com"
#git branch -M main 
#git remote add origin link do projeto
# git push -u origin main




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

#Como eu criei uma tabela de usuario eu tenho que dizer aqui qual é essa tabela
AUTH_USER_MODEL = "filme.Usuario" #nome da app e o nome da class que vc criou dentro da sua app
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/' #fromato dos arquivos

STATIC_ROOT = BASE_DIR / 'staticfiles' #PROCESSO DE DEPLOY whitenoise

STATICFILES_DIRS = [
    BASE_DIR / "static", # Fala onde vai ficar a sua pasta static, no caso vai ficar no diretorio
]

MEDIA_URL = 'media/' #Link

MEDIA_ROOT = BASE_DIR / 'media' # A pasta está recebendo esse nome, e ela está no diretório(pasta SITE-DJANGO)

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'filme:homefilmes'#link para quando o usuario fizer login ele ser redirecionado para homepage do site


LOGIN_URL = 'filme:login'#link onde vai está o template de login de usuario

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

#processo de deploy do nosso site
#intall duas bibliotecas no final deixar o debug = False se não ele pode divulgar coisas que não são pra serem divulgadas.
#pip install gunincorn
#pip install whitenoise é uma biblioteca do python que serve para configurar arquivos estáticos
#O servervidor precisa saber quais bibliotecas nós estamos usando
#pip freeze dá uma lista de tds bibliotecas que vc tá usando
#depois disso vc vai digitar
# pip freeze > requirements.txt