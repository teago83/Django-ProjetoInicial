from django.db import models

# Create your models here.

class Pergunta (models.Model):
    pergunta_text = models.CharField(max_length=200)
    publicacao_date = models.DateTimeField('date published')

class Escolha (models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    escolha_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)