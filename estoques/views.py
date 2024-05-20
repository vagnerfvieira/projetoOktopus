from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponse
from .models import Estoque, EstoqueItens
from .forms import EstoqueForm,EstoqueItensForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect


# Create your views here.

    
def entrada_estoque_list(request):
    estoques  = Estoque.objects.filter(movimento='e')
    return render(request, 'estoques/estoque_entrada_list.html', {'estoques':estoques})



def estoque_entrada_add(request):
    if request.method == 'GET':
        form = EstoqueForm()
        form_estoqueItens_factory = inlineformset_factory(Estoque, EstoqueItens, EstoqueItensForm, extra=1)
        form_estoqueItens = form_estoqueItens_factory()
        context = {
                'form': form,
                'form_estoqueItens': form_estoqueItens,
            }
            
        return render(request, 'estoques/estoque_entrada_add.html', context)
        
    elif request.method == 'POST':
        form = EstoqueForm(request.POST)
        form_estoqueItens_factory = inlineformset_factory(Estoque, EstoqueItens, EstoqueItensForm)
        form_estoqueItens = form_estoqueItens_factory(request.POST)
        if form.is_valid() and form_estoqueItens.is_valid():
            estoque = form.save()
            form_estoqueItens.instance = estoque
            form_estoqueItens.save()
            return redirect('estoque_entrada_add')
        else:
            context = {
                'form': form,
                'form_estoqueItens': form_estoqueItens,
            }
            
            return render(request, 'estoques/estoque_entrada_add.html', context)
        


def estoque_entrada_detail(request, id):
    estoque = get_object_or_404(Estoque, pk=id)
    form = EstoqueForm(instance=estoque)
    form_estoqueItens_factory = inlineformset_factory(Estoque, EstoqueItens, EstoqueItensForm, extra=3)
    form_estoqueItens = form_estoqueItens_factory(instance=estoque)
    
    context = {
        'form': form,
        'estoque': estoque,
        'form_estoqueItens': form_estoqueItens,

    }
    
    return render(request, 'estoques/estoque_entrada_detail.html', context)
