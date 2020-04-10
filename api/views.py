from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api import register


@api_view(['GET', 'POST'])
def pagamentos(request):
    """
    View para inserir pagamento ou obter todos os pagamentos.
    :param request: Requisição recebida pela view.
    :type request: object
    :return: Response
    :rtype: object
    """
    if request.method == 'POST':
        pgto = register.save_pagamentos(request)
        del pgto['_id']
        return Response(pgto)
    elif request.method == 'GET':
        pagamentos = register.get_pagamentos()
        return Response(pagamentos)
    else:
        return Response('Nenhum dado encontrato!', status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_pagamento(request):
    """
    View para atualização de pagamentos.
    :return: Response com status 202 ou 'Registro não atualizado' ou 405
    :rtype: object
    """
    if request.method == 'PUT':
        update = register.update_pagamento(request)
        if update == 1:
            return Response('Registro atualizado com sucesso.', status=status.HTTP_202_ACCEPTED)
        return Response('Registro não atualizado.')
    return Response(f'Operação não autorizada para o método {request.method}',
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)
