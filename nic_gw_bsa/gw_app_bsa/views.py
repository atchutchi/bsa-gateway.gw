from django.shortcuts import render
from django.http import JsonResponse
from .models import Dominio
from django.views.decorators.http import require_http_methods
import json
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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


# Função para autenticação e obtenção do token da API BSA
@csrf_exempt  # Desabilita a proteção CSRF para esta view específica
@require_http_methods(["POST"])
def autenticar_bsa(request):
    url = 'https://api-ote.bsagateway.co/iam/api/authenticate/apiKey'
    api_key = settings.BSA_API_KEY  # Armazene sua API Key em um local seguro, como uma variável de ambiente
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'apiKey': api_key, 'space': 'BSA'}
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        token = response.json().get('id_token')
        # Aqui você pode armazenar o token no banco de dados ou sessão conforme necessário
        return JsonResponse({'token': token})
    else:
        return JsonResponse({'error': 'Falha ao autenticar'}, status=401)