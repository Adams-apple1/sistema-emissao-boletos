from rest_framework import serializers
from .models import Emitente, Pagador, Boleto


class EmitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emitente
        fields = "__all__"


class PagadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagador
        fields = "__all__"


class BoletoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleto
        fields = "__all__"