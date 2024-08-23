from django.db import models

class terefa(models.Model):
    nome = models.CharField(max_length = 100)
    satus = models.CharField(max_length = 20)
    prazo = models.DateField()