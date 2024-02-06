from django.urls import path
from .views import listar_dominios, criar_dominio

# Definição das rotas para as views
urlpatterns = [
    path('dominios/', listar_dominios, name='listar_dominios'),  # Rota para listar domínios
    path('dominios/criar/', criar_dominio, name='criar_dominio'),  # Rota para criar um novo domínio
     path('autenticar_bsa/', autenticar_bsa, name='autenticar_bsa'),
]
