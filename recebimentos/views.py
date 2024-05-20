from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Recebimento
from .forms import RecebimentoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def listaRecebimento(request):
    
    search = request.GET.get('search')
    
    if search:
        recebimentos = Recebimento.objects(favorecido_icontains=search)
        
    else:
        recebimemtos_list = Recebimento.objects.all().order_by('-dt_real')
        paginator = Paginator(recebimemtos_list,5)
        page = request.GET.get('page')
        recebimentos = paginator.get_page(page)
        
    return render(request, 'recebimentos/listaRecebimento.html', {'recebimentos':recebimentos})


@login_required
def  viewRecebimento(request, id):
    recebimento = get_object_or_404(Recebimento, pk=id)
    return render(request, 'recebimentos/recebimento.html', {'recebimento':recebimento})

@login_required
def novoRecebimento(request):
    
    if request.method == 'POST':
        form = RecebimentoForm(request.POST)

        if form.is_valid():
            recebimento = form.save(commit=False)
            recebimento.done = 'doing'
            recebimento.save()
            return redirect('lista-recebimento')
    
    else:
         form = RecebimentoForm()
         return render(request, 'recebimentos/novoRecebimento.html', {'form':form}) 
              

@login_required
def editRecebimento(request, id):
    recebimento = get_object_or_404(Recebimento, pk=id)
    form = RecebimentoForm(instance=recebimento)
    
    if(request.method == 'POST'):
        form = RecebimentoForm(request.POST, instance=recebimento)
        if(form.is_valid()):
            recebimento.save()
            return redirect('lista-recebimento')
        else:
            return render(request, 'recebimentos/editRecebimento.html', {'form':form, 'recebimento':recebimento})
    else:
        return render(request, 'recebimentos/editRecebimento.html', {'form':form, 'recebimento':recebimento})
        
    
@login_required
def deleteRecebimento(request, id):
    recebimento = get_object_or_404(Recebimento, pk=id)
    recebimento.delete()
    
    messages.info(request, 'Recebimento excluído com sucesso !')
    
    return redirect('lista-recebimento')