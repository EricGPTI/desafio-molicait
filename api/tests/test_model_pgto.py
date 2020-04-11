from api.models import Pagamento, ConnectionDB
from decouple import config
from datetime import datetime
from pytest_mongodb.plugin import mongo_engine
from pytest import mark

conn = ConnectionDB(config('DB_HOST'), config('DB_PORT', cast=int))
db = conn.connection()


def test_pagamento(mongodb):
    assert 'pagamento' in mongodb.list_collection_names()
    id_pagamento = mongodb.pagamento.find_one({'id_pagamento': 'a5ddf4a2-33b9-4eae-b6f0-7b0dfba874ef'})
    assert id_pagamento['total'] == "100.00"


def test_model_qtd_cedula(mongodb):
    total = 85.92
    pago = 1000.00
    pagamento = Pagamento(total, pago)
    pgto = pagamento.pagamento()
    cedulas = pgto[0]
    assert cedulas['100.0'] == 9
    assert cedulas['10.0'] == 1
    assert cedulas['1.0'] == 4

def test_model_qtd_moedas(mongodb):
    total = 100.00
    pago = 150.15
    pagamento = Pagamento(total, pago)
    pgto = pagamento.pagamento()
    moedas = pgto[1]
    assert moedas['0.05'] == 1

def test_model_udpate_pagamento():
    id_pagamento = 'a5ddf4a2-33b9-4eae-b6f0-7b0dfba874ef'
    total = 100.00
    pago = 120.15
    pgto = Pagamento(total, pago)
    valores = pgto.pagamento()
    cedulas = str(valores[0])
    moedas = str(valores[1])
    data = datetime.now().strftime('%d/%m/%Y')

    u = {
        'id_pagamento': str(id_pagamento),
        'data': data,
        'total': str(total),
        'pago': str(pago),
        'troco': [cedulas, moedas]
    }
    update = Pagamento.update_pagamento(db, u)
    assert type(update.raw_result.get('nModified')) == int

