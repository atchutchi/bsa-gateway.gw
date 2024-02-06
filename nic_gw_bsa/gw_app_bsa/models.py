from django.db import models

# Modelo para representar um domínio .gw
class Dominio(models.Model):
    nome = models.CharField(max_length=255)  # Nome do domínio
    status = models.CharField(max_length=100)  # Status do domínio (e.g., 'disponível', 'registrado')
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação do registro
    data_atualizacao = models.DateTimeField(auto_now=True)  # Data de última atualização do registro

    def __str__(self):
        return self.nome  # Representação em string do modelo, usando o nome do domínio
