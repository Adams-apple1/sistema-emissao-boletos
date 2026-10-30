
from django.db import models


class Emitente(models.Model):
    razao_social = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14, unique=True)

    cooperativa = models.CharField(max_length=10)
    agencia = models.CharField(max_length=10)
    conta_corrente = models.CharField(max_length=20)

    numero_cliente = models.CharField(max_length=30)
    modalidade = models.CharField(max_length=10)
    convenio = models.CharField(max_length=30)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.razao_social


class Pagador(models.Model):
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=14, unique=True)

    email = models.EmailField(blank=True)

    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Boleto(models.Model):

    STATUS_CHOICES = [
        ("rascunho", "Rascunho"),
        ("registrado", "Registrado"),
        ("pago", "Pago"),
        ("vencido", "Vencido"),
        ("baixado", "Baixado"),
        ("erro", "Erro"),
    ]

    emitente = models.ForeignKey(
        Emitente,
        on_delete=models.PROTECT,
        related_name="boletos"
    )

    pagador = models.ForeignKey(
        Pagador,
        on_delete=models.PROTECT,
        related_name="boletos"
    )

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()

    seu_numero = models.CharField(max_length=18)
    numero_parcela = models.PositiveIntegerField(default=1)

    mensagem = models.TextField(blank=True)

    multa_percentual = models.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )

    juros_mes_percentual = models.DecimalField(
        max_digits=5, decimal_places=2, default=0
    )

    dias_protesto = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="rascunho"
    )

    nosso_numero = models.CharField(max_length=30, blank=True)
    linha_digitavel = models.CharField(max_length=100, blank=True)
    codigo_barras = models.CharField(max_length=100, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Boleto {self.seu_numero} - {self.pagador.nome}"

