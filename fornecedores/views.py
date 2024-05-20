from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Fornecedor
from .forms import FornecedorForm
from django.contrib import messages

# Create your views here.



def viewFornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    return render(request, 'fornecedores/fornecedor.html', {'fornecedor':fornecedor})

def novoFornecedor(request):
    
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        
        if form.is_valid():
            fornecedor = form.save(commit=False)
            fornecedor.save()
            return redirect('lista-fornecedor')        
    else:
            
        form = FornecedorForm()
        return render(request, 'fornecedores/novofornecedor.html', {'form':form})
    
def listaFornecedor(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/listafornecedor.html', {'fornecedores':fornecedores}) 

def editFornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    form = FornecedorForm(instance=fornecedor)
    
    if (request.method == 'POST'):
        
        if (request.method=='POST'):
            form = FornecedorForm(request.POST, instance=fornecedor)
            
            if (form.is_valid()):
                fornecedor.save()
                return redirect('lista-fornecedor')
    
            else:
                return render(request, 'fornecedores/editfornecedor.html', {'form':form, 'fornecedor':fornecedor})

    else:
        return render(request, 'fornecedores/editfornecedor.html', {'form':form, 'fornecedor':fornecedor})
