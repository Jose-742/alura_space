from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from galeria.models import Fotografia


@login_required(login_url='login')
def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

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
            

    return render(request, 'galeria/buscar.html',  {"cards": fotografias})