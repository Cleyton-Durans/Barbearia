from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nome


class Espera(models.Model):
    STATUS = [
        ('Aguardando', 'Aguardando'),
        ('Finalizado', 'Finalizado'),
    ]

    nome = models.CharField(max_length=100)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS, default='Aguardando')

    def __str__(self):
        return f"{self.nome} - {self.servico.nome} ({self.status})"
