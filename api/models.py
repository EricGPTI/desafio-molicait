from django.db import models
from pymongo import MongoClient
from decouple import config
from math import ceil


class ConnectionDB:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connection(self):
        client = MongoClient(self.host, self.port)
        db = client.molica
        return db


class Transacao:
    def __init__(self, total, pago):
        self.total = total
        self.pago = pago

    def pagamento(self):
        resto = self.pago - self.total
        if resto < 0:
            raise ValueError(f'{self.total} é maior que {self.pago}')
        elif resto == 0:
            return 0
        else:
            return round(resto, 2)

    @staticmethod
    def calcula_cedulas(resto):
        cedulas = [100.0, 50.0, 10.0, 5.0, 1.0]
        cont_cedulas = {'100.0': 0, '50.0': 0, '10.0': 0, '5.0': 0, '1.0': 0}
        for valor in cedulas:
            while resto >= valor:
                str_valor = str(valor)
                cont_cedulas[str_valor] += 1
                resto -= valor
                break
        return cont_cedulas, round(resto, 2)

    @staticmethod
    def calcula_moedas(resto):
        moedas = [0.5, 0.1, 0.05, 0.01]
        cont_moeda = {'0.5': 0, '0.1': 0, '0.05': 0, '0.01': 0}
        if resto > 0.00:
            for valor in moedas:
                while resto >= valor:
                    str_valor = str(valor)
                    cont_moeda[str_valor] += 1
                    resto -= round(valor, 2)
                    break
            return cont_moeda
        return cont_moeda
