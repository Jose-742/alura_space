from django.shortcuts import render, redirect

from django.shortcuts import render
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.POST:
        form = LoginForms(request.POST)
        if form.is_valid():
            nome=form['nome_login'].value()
            usuario = auth.authenticate(
                request,
                username=nome,
                password=form['senha'].value(),
            ) 
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')
    if request.GET:
        msg_next = request.GET.get('next')
        if msg_next:
            messages.warning(request, 'Usuário não logado')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.POST:
       form = CadastroForms(request.POST)
       if form.is_valid():
            usuario = User.objects.create_user(
                username=form['nome_cadastro'].value(),
                email=form['email'].value(),
                password=form['senha_1'].value(),
            )
            usuario.save()
            messages.success(request, f'Usuário {usuario.username} cadastrado com sucesso!')
            return redirect('cadastro')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, f'Logout efetuado com sucesso')
    return redirect('login')