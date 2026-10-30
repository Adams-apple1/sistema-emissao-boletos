
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Emitente, Pagador, Boleto
from .serializers import (
    EmitenteSerializer,
    PagadorSerializer,
    BoletoSerializer,
)


class EmitenteViewSet(viewsets.ModelViewSet):
    queryset = Emitente.objects.all()
    serializer_class = EmitenteSerializer


class PagadorViewSet(viewsets.ModelViewSet):
    queryset = Pagador.objects.all()
    serializer_class = PagadorSerializer


class BoletoViewSet(viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer

    @action(detail=True, methods=["post"])
    def emitir(self, request, pk=None):
        boleto = self.get_object()

        if boleto.status != "rascunho":
            return Response(
                {"erro": "Este boleto não está em rascunho e não pode ser emitido novamente."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Dados fictícios para simular a resposta do Sicoob
        boleto.nosso_numero = f"SIM-{boleto.id:08d}"
        boleto.linha_digitavel = f"SIMULADA-{boleto.id:010d}"
        boleto.codigo_barras = f"SIMULADO-{boleto.id:020d}"
        boleto.status = "registrado"

        boleto.save(update_fields=[
            "nosso_numero",
            "linha_digitavel",
            "codigo_barras",
            "status",
        ])

        return Response(
            {
                "mensagem": "Boleto emitido com sucesso em ambiente simulado.",
                "aviso": "Este boleto não foi registrado no banco Sicoob.",
                "boleto": BoletoSerializer(boleto).data,
            },
            status=status.HTTP_200_OK,
        )
