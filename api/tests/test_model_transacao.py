from api.models import Transacao
from math import ceil


def test_model_retorno_diferenca():
    total = 100.00
    pago = 150.00
    transacao = Transacao(total, pago)
    resto = transacao.pagamento()
    assert resto == 50.0


def test_model_qtd_cedula():
    total = 100.00
    pago = 150.00
    transacao = Transacao(total, pago)
    resto = transacao.pagamento()
    resto = ceil(resto)
    cedulas = transacao.calcula_cedulas(resto)[0]
    assert cedulas['50.0'] == 1

def test_model_qtd_moedas():
    total = 100.00
    pago = 150.15
    transacao = Transacao(total, pago)
    resto = transacao.pagamento()
    resto_cedulas = transacao.calcula_cedulas(resto)[1]
    moedas = transacao.calcula_moedas(resto_cedulas)
    assert moedas['0.05'] == 1


