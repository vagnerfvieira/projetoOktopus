from django.http import HttpResponse
from . models import PreçoVenda, PreçoVendaIten, Produto
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt



def preço_venda_calc(request):
     if request.method == "POST":
          quantidade = float(request.POST.get('preçoVenda-0-quantidade', 0))
          valorUnit = float(request.POST.get('preçoVenda-0-valorUnit', 0))
          descontos = float(request.POST.get('preçoVenda-0-descontos', 0))
          impostosNrec = float(request.POST('preçoVenda-0-impostosNrec', 0))
          impostosRec = float(request.POST('preçoVenda-0-impostosRec', 0))
          fretes = float(request.POST.get('preçoVenda-0-fretes', 0))
          seguros = float(request.POST.get('preçoVenda-0-seguros', 0))
          subsTrib = float(request.POST.get('preçoVenda-0-subsTrib', 0))
          outrosCustos = float(request.POST.get('preçoVenda-0-outrosCustos', 0))

          custoTotal = custo_total_resultado(quantidade, descontos,impostosNrec,impostosRec,fretes,seguros,subsTrib,outrosCustos)
          

          return render(request,'preçoVendas/preçoVenda_entrada_add.html', {'custoTotal':custoTotal})
    
     return render(request,'preçoVendas/preçoVenda_entrada_add.html')

    
def custo_total_resultado(quantidade, descontos,impostosNrec,impostosRec,fretes,seguros,subsTrib,outrosCustos):
    return (impostosNrec + impostosRec + fretes + seguros + subsTrib + outrosCustos - descontos) * quantidade
  