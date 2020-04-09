from api.models import Pagamento
from math import ceil


def test_model_qtd_cedula():
    total = 100.00
    pago = 150.00
    pagamento = Pagamento(total, pago)
    pgto = pagamento.pagamento()
    cedulas = pgto[0]
    assert cedulas['50.0'] == 1

def test_model_qtd_moedas():
    total = 100.00
    pago = 150.15
    pagamento = Pagamento(total, pago)
    pgto = pagamento.pagamento()
    moedas = pgto[1]
    assert moedas['0.05'] == 1