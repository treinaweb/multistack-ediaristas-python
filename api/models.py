import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from django.db.models.expressions import F
from localflavor.br.models import BRCPFField
from .managers import diarista_manager, diaria_manager, avaliacao_manager
from django.contrib.auth.models import UserManager
from administracao.models import Servico


# Create your models here.

def nome_arquivo_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)

    return os.path.join('usuarios', filename)

def nome_arquivo_documento(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)

    return os.path.join('documentos', filename)

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        (1, "Cliente"),
        (2, "Diarista")
    )

    username = None
    nome_completo = models.CharField(max_length=255, null=True, blank=False)
    cpf = BRCPFField(null=True, unique=True, blank=False)
    nascimento = models.DateField(null=True, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=False)
    tipo_usuario = models.IntegerField(choices=TIPO_USUARIO_CHOICES, null=True, blank=False)
    reputacao = models.FloatField(null=True, blank=False, default=5)
    chave_pix = models.CharField(null=True, blank=True, max_length=255)
    foto_documento = models.ImageField(null=True, upload_to=nome_arquivo_foto, 
    validators=[validate_image_file_extension, ])
    foto_usuario = models.ImageField(null=True, upload_to=nome_arquivo_documento, 
    validators=[validate_image_file_extension, ])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('nome_completo', 'cpf', 'telefone', 'tipo_usuario', 'reputacao',
    'chave_pix', 'foto_documento', 'foto_usuario')

    objects = UserManager()
    diarista_objects = diarista_manager.DiaristaManager()


class EnderecoDiarista(models.Model):
    logradouro = models.CharField(max_length=60, null=True, blank=False)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=30, null=False, blank=False)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=10, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    usuario = models.OneToOneField(Usuario, on_delete=models.DO_NOTHING, null=False, 
    blank=False, related_name='endereco')


class Diaria(models.Model):
    STATUS_DIARIA_CHOICES = (
        (1, "SEM_PAGAMENTO"),
        (2, "PAGO"),
        (3, "CONFIRMADO"),
        (4, "CONCLUIDO"),
        (5, "CANCELADO"),
        (6, "AVALIADO"),
        (7, "TRANSFERIDO")
    )

    data_atendimento = models.DateTimeField(null=False, blank=False)
    tempo_atendimento = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=False, choices=STATUS_DIARIA_CHOICES,
    default=1)
    preco = models.DecimalField(null=False, blank=False, 
    decimal_places=2, max_digits=5)
    valor_comissao = models.DecimalField(null=False, blank=False, 
    decimal_places=2, max_digits=5)    
    logradouro = models.CharField(max_length=60, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=30, null=False, blank=False)
    complemento = models.CharField(max_length=100, null=False, blank=True)
    cep = models.CharField(max_length=10, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    codigo_ibge = models.IntegerField(null=True, blank=True)
    quantidade_quartos = models.IntegerField(null=False, blank=False)
    quantidade_salas = models.IntegerField(null=False, blank=False)
    quantidade_cozinhas = models.IntegerField(null=False, blank=False)
    quantidade_banheiros = models.IntegerField(null=False, blank=False)
    quantidade_quintais = models.IntegerField(null=False, blank=False)
    quantidade_outros = models.IntegerField(null=False, blank=False)
    observacoes = models.TextField(null=False, blank=True)
    motivo_cancelamento = models.TextField(null=True, blank=True)
    cliente = models.ForeignKey(Usuario, null=False, blank=False, 
    on_delete=models.DO_NOTHING, related_name='cliente')
    diarista = models.ForeignKey(Usuario, null=True, blank=True, 
    on_delete=models.DO_NOTHING, related_name='diarista')
    servico = models.ForeignKey(Servico, null=False, blank=False, 
    on_delete=models.DO_NOTHING)
    candidatas = models.ManyToManyField(Usuario, blank=True, related_name='candidatas')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()
    diaria_objects = diaria_manager.DiariaManager()



class CidadesAtendimento(models.Model):
    codigo_ibge = models.IntegerField(null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    usuario = models.ManyToManyField(Usuario, related_name='cidades_atendidas')


class Pagamento(models.Model):
    status = models.CharField(max_length=20, null=False, blank=False)
    valor = models.DecimalField(null=False, blank=False, 
    decimal_places=2, max_digits=5)
    transacao_id = models.CharField(max_length=50, null=False, blank=False)
    diaria = models.ForeignKey(Diaria, null=False, blank=False, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class AvaliacaoDiaria(models.Model):
    descricao = models.TextField(null=False, blank=False)
    nota = models.FloatField(null=False, blank=False)
    visibilidade = models.IntegerField(null=False, blank=False)
    diaria = models.ForeignKey(Diaria, null=False, blank=False, on_delete=models.CASCADE,
    related_name='avaliacao_diaria')
    avaliador = models.ForeignKey(Usuario, null=True, blank=False, on_delete=models.CASCADE,
    related_name='avaliador')
    avaliado = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE,
    related_name='avaliado')

    objects = models.Manager()
    avaliacao_objects = avaliacao_manager.AvaliacaoManager()