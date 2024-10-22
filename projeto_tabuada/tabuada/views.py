from django.shortcuts import render
from django.http import HttpResponse #retorna texto em html

# Create your views here.
def semnum(request):
    return HttpResponse("<h1>ERRO! Você não colocou numero nenhum.</h1><h3>Use depois da url /tabuada/numero</h3><br><h3>exemplo: http://127.0.0.1:8000/tabuada/5 e irá aparecer a tabuada do numero 5</h3>")

def tabuada(request, num): #requisição htpp feita pelo navegador e o num passado na url
    html = '<table border="2">' 
    for i in range(1,11):
        html += f'<tr><td>{num} x {i}</td><td>{num * i}</td></tr>'
        html += '</table>'

    return HttpResponse(f"<h1>Tabuada do {num}</h1>" + html) 
        