from django.shortcuts import render,redirect
from .forms import ContratoForm
from .models import Contrato

# Create your views here.

def Home(request):
    return render(request,'index.html')

def crearContrato(request):
    if request.method == 'POST':
        contrato_form = ContratoForm(request.POST)
        if contrato_form.is_valid():
            contrato_form.save()
            return redirect('index')
    else:
        contrato_form = ContratoForm()
    return render(request,'contrato/crear_contrato.html',{'contrato_form':contrato_form})

def listarContrato(request):
    contratos = Contrato.objects.all()
    return render(request, 'contrato/listar_contrato.html', {'contratos':contratos})

def editarContrato(request, id_contrato):
    contrato = Contrato.objects.get(id_contrato = id_contrato)
    if request.method == 'GET':
        contrato_form = ContratoForm(instance = contrato)
    else:
        contrato_form = ContratoForm(request.POST, instance = contrato)
        if contrato_form.is_valid():
            contrato_form.save()
        return redirect('index')
    return render(request,'contrato/crear_contrato.html',{'contrato_form':contrato_form})

def eliminarContrato(request, id_contrato):
    contrato = Contrato.objects.get(id_contrato = id_contrato)
    if request.method == 'POST':
        contrato.delete()
        return redirect('contrato:listar_contrato')
    return render(request,'contrato/eliminar_contrato.html',{'contrato':contrato})

