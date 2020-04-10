from api.models import Pagamento, ConnectionDB
from decouple import config

conn = ConnectionDB(config('DB_HOST'), config('DB_PORT', cast=int))
db = conn.connection()

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

def test_model_udpate_pagamento():
    session = 'd69fbed7-a802-442b-9ddb-10d42abf899f'
    pgto = Pagamento.update_pagamento(db, session)
