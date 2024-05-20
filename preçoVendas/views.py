from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponse
from .models import PreçoVenda, PreçoVendaIten
from .forms import PreçoVendaForm,PreçoVendaItenForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def preçoVendas_list(request):
    preçoVendas  = PreçoVenda.objects.all()
    return render(request, 'preçoVendas/preçoVendas_list.html', {'preçoVendas':preçoVendas})


def preçoVenda_add(request):
    if request.method == 'GET':
        form = PreçoVendaForm()
        form_preçoVendasItens_factory = inlineformset_factory(PreçoVenda, PreçoVendaIten, PreçoVendaItenForm, extra=1)
        form_preçoVendaItens = form_preçoVendasItens_factory()
        context = {
                'form': form,
                'form_preçoVendaItens': form_preçoVendaItens,
            }
            
        return render(request, 'preçoVendas/preçoVenda_add.html', context)
        
    elif request.method == 'POST':
        form = PreçoVendaForm(request.POST)
        form_preçoVendasItens_factory = inlineformset_factory(PreçoVenda, PreçoVendaIten, PreçoVendaItenForm)
        form_preçoVendaItens = form_preçoVendasItens_factory(request.POST)
        if form.is_valid() and form_preçoVendaItens.is_valid():
            preçoVenda = form.save()
            form_preçoVendaItens.instance = preçoVenda
            form_preçoVendaItens.save()
            return redirect('preçoVendas_list')
        else:
            context = {
                'form': form,
                'form_preçoVendaItens': form_preçoVendaItens,
            }
            
        return render(request, 'preçoVendas/preçoVenda_add.html', context)
    
 
def preçoVenda_edit(request, id):
    if request.method == 'GET':
        objeto = PreçoVenda.objects.filter(pk=id).first()
        if objeto is None:
            return redirect(reverse('preçoVendas_list'))
        
        form = PreçoVendaForm(instance=objeto)
        form_preçoVendasItens_factory = inlineformset_factory(PreçoVenda, PreçoVendaIten, form= PreçoVendaItenForm, extra=0)
        form_preçoVendaItens = form_preçoVendasItens_factory(instance=objeto)
        context = {
                        'form': form,
                        'form_preçoVendaItens': form_preçoVendaItens,
                }
            
        return render(request, 'preçoVendas/preçoVenda_add.html', context)
        
    elif request.method == 'POST':
        objeto = PreçoVenda.objects.filter(pk=id).first()
        if objeto is None:
            return redirect(reverse('preçoVendas_list'))

        form = PreçoVendaForm(request.POST, instance=objeto)
        form_preçoVendasItens_factory = inlineformset_factory(PreçoVenda, PreçoVendaIten, form= PreçoVendaItenForm, extra=0)
        form_preçoVendaItens = form_preçoVendasItens_factory(request.POST, instance=objeto)
        if form.is_valid() and form_preçoVendaItens.is_valid():
            preçoVenda = form.save()
            form_preçoVendaItens.instance = preçoVenda
            form_preçoVendaItens.save()
            return redirect(reverse('preçoVendas_list'))
        else:
            context = {
                'form': form,
                'form_preçoVendaItens': form_preçoVendaItens,
            }
            
        return render(request, 'preçoVendas/preçoVenda_add.html', context)

def preçoVenda_delete(request, id):
    preçoVenda = get_object_or_404(PreçoVenda, pk=id)
    preçoVenda.delete()
    
    messages.info(request, 'Despesa excluída com sucesso !')
    return redirect('preçoVendas_list')
