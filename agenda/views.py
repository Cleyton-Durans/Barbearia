from django.shortcuts import render, redirect, get_object_or_404
from .models import Servico, Espera
from .forms import EsperaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    servicos = Servico.objects.all()
    if request.method == 'POST':
        form = EsperaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EsperaForm()
    return render(request, 'index.html', {'form': form, 'servicos': servicos})

@login_required
def lista(request):
    esperas = Espera.objects.order_by('data', 'hora')
    return render(request, 'lista.html', {'esperas': esperas})

@login_required
def finalizar(request, espera_id):
    espera = get_object_or_404(Espera, pk=espera_id)
    espera.status = 'Finalizado'
    espera.save()
    return redirect('lista')

@login_required
def logout(request):
    logout(request)
    return redirect('index')
