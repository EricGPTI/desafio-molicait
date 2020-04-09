from api.models import Pagamento, ConnectionDB
import uuid
from decouple import config
from datetime import datetime

def save_pagamento(request):
    session = uuid_generate()
    total = request.data.get('total')
    pago = request.data.get('pago')

    conn = ConnectionDB(config('DB_HOST'), config('DB_PORT', cast=int))
    db = conn.connection()
    pgto = Pagamento(total, pago)
    valores = pgto.pagamento()
    cedulas = str(valores[0])
    moedas = str(valores[1])
    data = datetime.now().strftime('%d/%m/%Y')

    p = {
        'session': str(session),
        'data': data,
        'total': str(total),
        'pago': str(pago),
        'troco': [cedulas, moedas]
    }
    pgto.save_pgto(db, p)
    return p


def get_pagamento(session):
    pass


def uuid_generate():
    session = uuid.uuid4()
    return session