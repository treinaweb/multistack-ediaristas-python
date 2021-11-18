from django.db.models import fields
from rest_framework import serializers
from ..models import Pagamento

class PagamentoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    valor_deposito = serializers.SerializerMethodField()
    
    class Meta:
        model = Pagamento
        fields = ('id', 'status', 'valor', 'valor_deposito', 'created_at')

    def get_status(self, obj):
        if obj.diaria.status == 4 or obj.diaria.status == 6:
            return 2
        else:
            return 1

    def get_valor_deposito(self, obj):
        return obj.valor - obj.diaria.servico.porcentagem_comissao