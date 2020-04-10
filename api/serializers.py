from rest_framework import serializers
from .models import Pagamento
import json


class PagamentoSerializer:
    def __init__(self, pgto):
        self.pgto = pgto
        
    def serialize(self):
        data = json.dumps(self.pgto)
        return data