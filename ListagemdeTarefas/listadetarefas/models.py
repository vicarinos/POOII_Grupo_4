from django.db import models


class Responsavel(models.Model):
    nome = models.CharField(max_length=100, null=False, blank = False)
    num_cpf=models.CharField(max_length=11, null=False, blank=False)

class tarefa(models.Model):
    titulo = models.CharField(max_length= 100, null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, null= False, blank=False)
    prazoLimite = models.DateTimeField(null = False, blank=False)
    terminado_em = models.DateTimeField(null=True)
    pessoa_responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)

<<<<<<< HEAD
class mestre_dos_magos(models.Model):
    name = models.CharField(max_length=100, null=False, blank = False)
    deu_aula = models.DateTimeField(auto_now_add=True, null= False, blank=False)


# Create your models here.
=======
class ferias(models.Model):
    prazoinicio = models.DateTimeField(null = False, blank=False)
    prazofinal = models.DateTimeField(null = False, blank=False)
>>>>>>> 43990852d97e7ea3a179f34fbf613aa750aad813
class v(models.Model):
    titulo = models.CharField(max_length= 100, null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, null= False, blank=False)

# Create your models here.
class ferias(models.Model):
    prazoinicio = models.DateTimeField(null = False, blank=False)
    prazofinal = models.DateTimeField(null = False, blank=False)


class grupo_da_sala(models.Model):
    nome1 = models.CharField(max_length= 100, null=False, blank=False)
    nome2 = models.CharField(max_length= 100, null=False, blank=False)
    nome3 = models.CharField(max_length= 100, null=False, blank=False)
    nome4 = models.CharField(max_length= 100, null=False, blank=False)
