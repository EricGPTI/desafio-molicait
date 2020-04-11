from api.models import Pagamento, ConnectionDB
import uuid
from decouple import config
from datetime import datetime


conn = ConnectionDB(config('DB_HOST'), config('DB_PORT', cast=int))
db = conn.connection()


def save_pagamento(request):
    """
    Função que gera id para a sessão(identificador da transação), monta o modelo de dados para salvamento de pagamento.
    :param request: Requisição feita.
    :type request: object
    :return: Retorna o modelo de dados que foi salvo para apresentação.
    :rtype: dict
    """
    id_pagamento = uuid_generate()
    total = request.data.get('total')
    pago = request.data.get('pago')

    pgto = Pagamento(total, pago)
    valores = pgto.pagamento()
    cedulas = str(valores[0])
    moedas = str(valores[1])
    data = datetime.now().strftime('%d/%m/%Y')

    p = {
        'id_pagamento': str(id_pagamento),
        'data': data,
        'total': str(total),
        'pago': str(pago),
        'troco': [cedulas, moedas]
    }
    save_result = pgto.save_pagamento(db, p)
    if save_result is True:
        return p


def get_pagamentos():
    """
    Função que solicita a consulta ao modelo de dados de todos os pagamentos.
    :return: Retorna uma lista com todos os pagamentos.
    :rtype: list
    """
    pagamentos = Pagamento.get_pagamentos(db)
    return pagamentos


def update_pagamento(request):
    """
    Função para preparação dos dados para udpate.
    :param request: Requisição de update
    :type request: object
    :return: Retorno 1 se houve atualização ou 0 caso não.
    :rtype: int
    """
    if request.data.get('id') is not None:
        id_pagamento = request.data.get('id_pagamento')
        total = request.data.get('total')
        pago = request.data.get('pago')

        pagamento_salvo = Pagamento.get_pagamento(db, id_pagamento)
        total_salvo = pagamento_salvo.get('total')
        pago_salvo = pagamento_salvo.get('pago')

        if total is None:
            total = total_salvo

        if pago is None:
            pago = pago_salvo

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
        update_result = Pagamento.update_pagamento(db, u)
        registro_modificado = update_result.raw_result.get('nModified')
        return registro_modificado
    return None

def delete_pagamento(request, id_pagamento):
    """
    Função para registrar o modelo de dados para deleção.
    :param request: Request da requisição web.
    :type request: object
    :param id: Número que identifica a transação a ser deletada.
    :type id:
    :return:
    :rtype:
    """
    if request.method == 'DELETE':
        deleted = Pagamento.delete_pagamento(db, id_pagamento)
        return deleted


def uuid_generate():
    """
    Gera id da transação (id)
    :return: Retorna Id da transação gerado.
    :rtype: object
    """
    id = uuid.uuid4()
    return id
