from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=20, unique=True)
    data_admissao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome
