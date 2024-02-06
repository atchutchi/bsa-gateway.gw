from django.shortcuts import render
from django.http import JsonResponse
from .models import Dominio
from django.views.decorators.http import require_http_methods
import json

# View para listar todos os domínios
@require_http_methods(["GET"])
def listar_dominios(request):
    dominios = Dominio.objects.all()  # Consulta todos os domínios
    # Serializa e retorna os dados dos domínios em formato JSON
    return JsonResponse(list(dominios.values()), safe=False)

# View para criar um novo domínio
@require_http_methods(["POST"])
def criar_dominio(request):
    dados = json.loads(request.body)  # Carrega os dados do corpo da requisição
    dominio = Dominio.objects.create(nome=dados['nome'], status=dados['status'])  # Cria um novo registro de domínio
    # Retorna os dados do domínio criado em formato JSON
    return JsonResponse({'id': dominio.id, 'nome': dominio.nome, 'status': dominio.status})
