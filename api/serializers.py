from rest_framework import serializers
from .models import Pagamento
from django.core.serializers.json import DjangoJSONEncoder


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Pagamento
        fields: ('sessio', 'data', 'total', 'pago', 'troco')
