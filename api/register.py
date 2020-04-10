from api.models import Pagamento, ConnectionDB
import uuid
from decouple import config
from datetime import datetime


conn = ConnectionDB(config('DB_HOST'), config('DB_PORT', cast=int))
db = conn.connection()



def save_pagamento(request):
    session = uuid_generate()
    total = request.data.get('total')
    pago = request.data.get('pago')

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


def get_pagamentos():
    pagamentos = Pagamento.get_pagamentos(db)
    return pagamentos


def update_pagamento(request):
    if request.data.get('session') is not None:
        session = request.data.get('session')
        total = request.data.get('total')
        pago = request.data.get('pago')

        pagamento_salvo = Pagamento.get_pagamento(db, session)
        total_salvo = pagamento_salvo.get('total')
        pago_salvo = pagamento_salvo.get('pago')

        if total is not None:
            if pago is not None:
                pgto = Pagamento(total, pago)
                valores = pgto.pagamento()
                cedulas = str(valores[0])
                moedas = str(valores[1])
                data = datetime.now().strftime('%d/%m/%Y')

                u = {
                    'session': str(session),
                    'data': data,
                    'total': str(total),
                    'pago': str(pago),
                    'troco': [cedulas, moedas]
                }
                update_result = Pagamento.update_pagamento(db, u)
                registro_modificado = update_result.raw_result.get('nModified')
                return registro_modificado
    return None



def uuid_generate():
    session = uuid.uuid4()
    return session