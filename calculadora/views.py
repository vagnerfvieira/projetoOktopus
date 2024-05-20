from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#este não precisa de nada nesta função, funciona somente com return
def home(request):
    if request.method=="POST":
        numero1 = float(request.POST.get('numero1', 0))
        numero2 = float(request.POST.get('numero2', 0))
        operação = request.POST.get('operação')

        resultado = calcular_resultado_(numero1,numero2,operação)

        return render(request,'calc/home.html', {'resultado':resultado})
    
    return render(request,'calc/home.html')
    

def calculate(request):
    if request.method=="POST":
        numero1 = float(request.POST.get('numero1', 0))
        numero2 = float(request.POST.get('numero2', 0))
        operação = request.POST.get('operação')

        resultado = calcular_resultado_(numero1,numero2,operação)

        return render(request,'calc/home.html', {'resultado':resultado})
    return HttpResponse("invalida")

def calcular_resultado_(numero1, numero2, operação):
    if operação == "somar":
        return numero1 + numero2
    
    elif operação == "subtrair":
        return numero1 - numero2
    
    elif  operação == "multiplicar":
        return numero1 * numero2
    
    elif operação == 'dividir':
        if numero2 != 0:
            return numero1/numero2
        else:
            return 'erro: divisão por zero'
    else:
        return 'erro: operação invalida'

