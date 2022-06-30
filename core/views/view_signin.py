from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, "core/index.html")

def signin_page(request):
    return render(request, 'core/signin.html')

def signout_page(request):
    logout(request)
    return redirect('/signin_page/')

def login_page(request):
    if request.POST:
        username = request.POST.get('username') # Recuperando os parametros enviados pelo formulário
        password = request.POST.get('password') # Recuperando os parametros enviados pelo formulário

        usuario = authenticate(username=username, password=password) # Fazendo a autenticação
        if usuario is not None:
            login(request, usuario)
            return redirect('/index/')
        else:
            messages.error(request, "Usuário ou senha invalido!")
    return redirect('/index/')


# @login_required(login_url='/signin_page/', )
@login_required()
def index(request):
    # url = settings.URL_ENV_FAVORITES
    # aux = requests.get(url)
    # dts = aux.json()

    # context = {  
    #     'dts': dts,
    # }
    # return render(request, 'core/index.html', context)
    return render(request, 'core/index.html')