from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receita(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.IntegerField()
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True) 
    foto_receita = models.ImageField(upload_to='receitas/fotos', blank=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo