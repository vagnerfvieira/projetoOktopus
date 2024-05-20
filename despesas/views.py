from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Despesa
from .forms import DespesaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def listaDespesa(request):
    
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    
    if search:
        
        despesas = Despesa.objects.filter(favorecido__icontains=search)
        
    elif filter:
        
        despesas = Despesa.objects.filter(done=filter, user=request.user)
    
    else:
    
        despesas_list = Despesa.objects.all().order_by('-dt_real')   
        paginator = Paginator(despesas_list, 7)
        page = request.GET.get('page')
        despesas = paginator.get_page(page)
        
    return render(request, 'despesas/lista.html', {'despesas':despesas})

@login_required
def viewDespesa(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    return render(request, 'despesas/despesa.html', {'despesa':despesa})

@login_required
def novaDespesa(request):
    
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        
        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.done = 'doing'
            despesa.save()
            return redirect('lista-despesa')        
    else:
            
        form = DespesaForm()
        return render(request, 'despesas/novadespesa.html', {'form':form})
    
@login_required
def editDespesa(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    form = DespesaForm(instance=despesa)
    
    if (request.method=='POST'):
        form = DespesaForm(request.POST, instance=despesa)
        if (form.is_valid()):
            despesa.save()
            return redirect('lista-despesa')
        else:
            return render(request, 'despesas/editDespesa.html', {'form':form, 'despesa':despesa})
            ##procurar inserir erros de seção no prograama
    
    else:
        return render(request, 'despesas/editDespesa.html', {'form':form, 'despesa':despesa})
    
@login_required
def deleteDespesa(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    despesa.delete()
    
    messages.info(request, 'Despesa excluída com sucesso !')
    return redirect('lista-despesa')

@login_required
def changeStatus(request, id):
    despesa = get_object_or_404(Despesa, pk=id)
    
    if(despesa.done == 'doing'):
        despesa.done = 'done'
    else:
        despesa.done = 'doing'
    
    despesa.save()
    return redirect('/')
        

def helloWorld(request):
    return HttpResponse('teste')