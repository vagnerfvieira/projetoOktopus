from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Empresa
from .forms import EmpresaForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.



def listaEmpresa(request):
    empresa_list = Empresa.objects.all().order_by('-nome')
    paginator = Paginator(empresa_list, 3)
    page = request.GET.get('page')
    empresas = paginator.get_page(page)
    return render(request, 'empresas/listaempresa.html', {'empresas':empresas})


def viewEmpresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    return render(request, 'empresas/empresa.html', {'empresa':empresa})


def novaEmpresa(request):
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        
        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.save()
            return redirect('lista-empresa')        
    else:
            
        form = EmpresaForm()
        return render(request, 'empresas/novaempresa.html', {'form':form})

def deleteEmpresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    empresa.delete()
    
    messages.info(request, 'Empresa excluída com sucesso !')
    
    return redirect('lista-empresa')


def editEmpresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    form = EmpresaForm(instance=empresa)
    
    if (request.method=='POST'):
        form = EmpresaForm(request.POST, instance=empresa)
        if (form.is_valid()):
            empresa.save()
            return redirect('lista-empresa')
        else:
            return render(request, 'empresas/editEmpresa.html', {'form':form, 'empresa':empresa})
        
    else:
            return render(request, 'empresas/editEmpresa.html', {'form':form, 'empresa':empresa})