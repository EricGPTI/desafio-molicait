from rest_framework import serializers
from api.models import Transacao


class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['_id', 'total', 'pago', 'troco', 'session', 'date']

