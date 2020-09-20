from django.http import HttpResponse
from django.shortcuts import render
from .models import Produto

# Create your views here.

# def home(request):
#     return HttpResponse("Olá, Django! Finalmente!")

def index(request):
    produtos = Produto.objects.all()

    context = {
        "curso": "Programação web com framework django. \o/",
        "texto2": "Ainda tentando ver se carrega em seguida.",
        "produtos": produtos
    }

    return render(request, "index.html", context)


def contato(request):
    return render(request, "contato.html")


def produto(request, pk):
    print(f"pk: {pk}")
    produto_selecionado = Produto.objects.get(id=pk)

    context = {
        "produto": produto_selecionado
    }

    return render(request, 'produto.html', context)