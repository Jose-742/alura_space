from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms


@login_required(login_url='login')
def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

@login_required(login_url='login')
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

@login_required(login_url='login')
def buscar(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        buscar = request.GET.get('buscar')
        if buscar:
            fotografias = fotografias.filter(nome__icontains=buscar)
            

    return render(request, 'galeria/index.html',  {"cards": fotografias})

@login_required(login_url='login')
def nova_imagem(request):
    form = FotografiaForms()
    if request.POST:
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada')
            return redirect('index')
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.POST:
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": fotografias})