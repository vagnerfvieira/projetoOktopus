import pandas as pd


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Produto
from .forms import ProdutoForm, ImportarDadosForm
from django.contrib import messages
from django.views.generic import CreateView
from django.views import View
# Create your views here.


def viewProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'produtos/produto.html', {'produto':produto})

def novoProduto(request):
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('lista-produto')     
    else:
            
        form = ProdutoForm()
        return render(request, 'produtos/novoproduto.html', {'form':form})


def listaProduto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listaproduto.html', {'produtos':produtos})


def editProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(instance=produto)
    
    if (request.method == 'POST'):
        
        if (request.method=='POST'):
            form = ProdutoForm(request.POST, instance=produto)
            
            if (form.is_valid()):
                produto.save()
                return redirect('lista-produto')
    
            else:
                return render(request, 'produtos/editproduto.html', {'form':form, 'produto':produto})

    else:
        return render(request, 'produtos/editproduto.html', {'form':form, 'produto':produto})

class importarDadosProdutos(View):
    template_name = 'produtos/importarDadosProduto.html'

    def get(self, request):
        produtos = Produto.objects.all()
        form = ImportarDadosForm()
        return render(request, self.template_name, {
            'form': form,
            'produtos': produtos})
    
    def post(self, request):
        form = ImportarDadosForm(request.POST, request.FILES)

        if form.is_valid():
            arquivo = request.FILES['arquivo']
            df = pd.read_excel(arquivo)

            for _, row in df.iterrows():
                # Itera sobre as linhas do DataFrame lido do arquivo Excel 
                
                self.criar_produto(row)

            return redirect('importar_Dados')

        return render(request, self.template_name, {'form': form})
    
    def criar_produto(self, row):
        # Use get_or_create para evitar a necessidade de verificar a existência antes de criar
        produto = Produto.objects.get_or_create(
            docto=row['docto'],
            defaults={
                'produto': row['produto'],
                'qtde': row['qtde'],
                'importado': row['importado'],
                'valorUn': row['valorUn']
            }
        )

