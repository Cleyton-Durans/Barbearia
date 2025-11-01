from django.shortcuts import render, redirect, get_object_or_404
from .models import Servico, Espera
from .forms import EsperaForm

def index(request):
    servicos = Servico.objects.all()
    if request.method == 'POST':
        form = EsperaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = EsperaForm()
    return render(request, 'index.html', {'form': form, 'servicos': servicos})


def lista(request):
    esperas = Espera.objects.order_by('data', 'hora')
    return render(request, 'lista.html', {'esperas': esperas})


def finalizar(request, espera_id):
    espera = get_object_or_404(Espera, pk=espera_id)
    espera.status = 'Finalizado'
    espera.save()
    return redirect('lista')
