from django.urls import path
from .views import (listar_dominios, criar_dominio, autenticar_bsa,
                    AtualizarNomesIndisponiveisView, RecuperarSubordensPendentesView)

# Definição das rotas para as views
urlpatterns = [
    path('dominios/', listar_dominios, name='listar_dominios'),  # Rota para listar domínios
    path('dominios/criar/', criar_dominio, name='criar_dominio'),  # Rota para criar um novo domínio
    path('autenticar_bsa/', autenticar_bsa, name='autenticar_bsa'),
    path('nomes_indisponiveis/atualizar/', AtualizarNomesIndisponiveisView.as_view(), name='atualizar_nomes_indisponiveis'),
    path('subordens/recuperar/', RecuperarSubordensPendentesView.as_view(), name='recuperar_subordens_pendentes'),
]
