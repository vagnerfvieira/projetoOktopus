from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Cliente, Telefone
from .forms import ClienteForm, TelefoneForm
from django.forms import inlineformset_factory
from django.contrib import messages

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView



def viewCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)
    form_telefone_factory = inlineformset_factory(Cliente, Telefone, TelefoneForm, extra=3)
    form_telefone = form_telefone_factory(instance=cliente)
    
    context = {
        'form': form,
        'cliente': cliente,
        'form_telefone': form_telefone,

    }
    
    return render(request, 'clientes/cliente.html', context)

##########################################################################################################

def novoCliente(request):
    
    if request.method == 'GET':
        form = ClienteForm()
        form_telefone_factory = inlineformset_factory(Cliente, Telefone, TelefoneForm, extra=3)
        form_telefone = form_telefone_factory()
        context = {
                'form': form,
                'form_telefone': form_telefone,
            }
            
        return render(request, 'clientes/novocliente.html', context)
    
    elif  request.method == 'POST':
        form = ClienteForm(request.POST)
        form_telefone_factory = inlineformset_factory(Cliente, Telefone, TelefoneForm)
        form_telefone = form_telefone_factory(request.POST)
        if form.is_valid() and form_telefone.is_valid():
            cliente = form.save()
            form_telefone.instance = cliente
            form_telefone.save()
            return redirect('lista-cliente')        
        else:
            
             context = {
                'form': form,
                'form_telefone': form_telefone,
            }
                
  
             return render(request, 'clientes/novocliente.html', context)
    
#################################################################################################################
       
def listaCliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listacliente.html', {'clientes':clientes}) 

################################################################################################################
def editCliente(request, id):
    if request.method == "GET":
        objeto = Cliente.objects.filter(pk=id).first()
        if objeto is None:
            return redirect(reverse('lista-cliente'))
        form = ClienteForm(instance=objeto)
        form_telefone_factory = inlineformset_factory(Cliente,Telefone, form=TelefoneForm, extra=1)
        form_telefone = form_telefone_factory(instance=objeto)
        context = {
            'form': form,
            'form_telefone': form_telefone,
        }
        return render(request, 'clientes/editcliente.html', context)
    
    elif request.method == "POST":
        objeto = Cliente.objects.filter(pk=id).first()
        if objeto is None:
            return redirect(reverse('lista-cliente'))
        form = ClienteForm(request.POST, instance=objeto)
        form_telefone_factory = inlineformset_factory(Cliente, Telefone, TelefoneForm)
        form_telefone = form_telefone_factory(request.POST, instance=objeto)
        
        if form.is_valid() and form_telefone.is_valid():
            form.save()
            form_telefone.save()
            return redirect(reverse('lista-cliente'))
        else:
            context = {
            'form': form,
            'form_telefone':form_telefone,
        }
        return render(request, 'clientes/editcliente.html', context)
            