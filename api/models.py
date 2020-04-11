from pymongo import MongoClient


class ConnectionDB:
    """
    Classe de conexão com o banco de dados.
    """
    def __init__(self, host, port):
        """
        Contrutor da classe ConnectionDB
        :param host: Endereço IP do Banco de Dados.
        :type host: str
        :param port: Porta de conexão com o Banco de Dados.
        :type port: int
        """
        self.host = host
        self.port = port

    def connection(self):
        """
        Método que faz a conexão com o banco de dados.
        :return: Retorna a conexão com o banco de dados.
        :rtype:
        """
        conn = MongoClient(self.host, self.port)
        db = conn.molica
        return db


class Pagamento:
    """
    Classe para processar pagamentos.
    """
    def __init__(self, total, pago):
        """
        Construtor da classe Pagamento.
        :param total: Total do pagamento.
        :type total: str
        :param pago: Valor pago.
        :type pago: str
        """
        self.total = float(total)
        self.pago = float(pago)

    def pagamento(self):
        """
        Faz o cálculo da diferença entre o valor da pago -
        :return: Retorna a diferença entre entre pago e total. Irá retornar raise ValueError caso o valor pago seja
        menor que o total ou quantidade de cédulas e moedas.
        :rtype: raiser ValueError ou tuple de dicionários.
        """
        if float(self.pago ) < float(self.total):
            raise ValueError(f'Valor pago - {self.pago} é menor que total {self.total}')
        else:
            resto = round(float(self.pago - self.total), 2)
            pgto_obj = self.calcula_cedulas(resto)
            resto_cedulas = pgto_obj[1]
            cedulas = pgto_obj[0]
            moedas = self.calcula_moedas(resto_cedulas)
            return cedulas, moedas

    def calcula_cedulas(self, resto):
        """
        Calcula a quantidade de cédulas que deve ser dada como troco de acordo com o resto da subtração
        entre pago - total.
        :param resto: Resto da subtração de pago - total.
        :type resto: float
        :return: Tupla contendo dicionário e o resto que sobrou após cálculo das cédulas.
        :rtype: Tupla contendo dicionário de cedulas e o resto.
        """
        cedulas = [100.0, 50.0, 10.0, 5.0, 1.0]
        cont_cedulas = {'100.0': 0, '50.0': 0, '10.0': 0, '5.0': 0, '1.0': 0}
        for valor in cedulas:
            while resto >= valor:
                str_valor = str(valor)
                cont_cedulas[str_valor] += 1
                resto -= valor
        return cont_cedulas, round(resto, 2)

    def calcula_moedas(self, resto):
        moedas = [0.50, 0.10, 0.05, 0.01]
        cont_moedas = {'0.5': 0, '0.1': 0, '0.05': 0, '0.01': 0}
        for valor in moedas:
            while round(resto, 2) >= valor:
                str_valor = str(valor)
                cont_moedas[str_valor] += 1
                resto -= round(valor, 2)
        return cont_moedas

    @staticmethod
    def save_pagamento(db, p):
        """
        Método estático para salvamento de um  pagamento.
        :param db: Conexão com o banco de dados.
        :type db: object
        :param p: Modelo de dados contendo informações de pagamento
        :type p: dict
        :return:
        :rtype:
        """
        result_pagamento = db.pagamento.insert_one(p)
        return result_pagamento

    @staticmethod
    def get_pagamentos(db):
        """
        Método estático para consulta de todos os pagamentos.
        :param db: Instância de banco de dados.
        :type db: object
        :return: Lista de todos os pagamentos.
        :rtype: list
        """
        pgto = db.pagamento.find()
        pagamento = []
        for p in pgto:
            del p['_id']
            pagamento.append(p)
        return pagamento

    @staticmethod
    def get_pagamento(db, id_pagamento):
        """
        Método estático para consulta de um pagamento específico pelo id_pagamento.
        :param db: Instância do banco de dados.
        :type db: object
        :param id_pagamento: Id da transação.
        :type id_pagamento: str
        :return: Retorna um pagamento específico.
        :rtype:
        """
        pagamento = db.pagamento.find_one({'id_pagamento': id_pagamento})
        return pagamento


    @staticmethod
    def update_pagamento(db, u):
        """
        Método estático para update de um registro de pagamento.
        :param db: Instância de banco de dados.
        :type db: object
        :param u: Registro para update
        :type u: dict
        :return: Retorna UpdateResult
        :rtype: object
        """
        id_pagamento = u['id_pagamento']
        reg_update = Pagamento.get_pagamento(db, id_pagamento)
        new_data = {'$set': u}
        pagamento_updated = db.pagamento.update_one(reg_update, new_data)
        return pagamento_updated


    @staticmethod
    def delete_pagamento(db, id_pagamento):
        """
        Método estático para deleção de um pagamento.
        :param db: Instância de banco de dados.
        :type db: object
        :param id_pagamento: Id da transação de pagamento.
        :type id_pagamento: str
        :return:
        :rtype:
        """
        id_delete = {'id_pagamento': id_pagamento}
        deleted = db.pagamento.delete_one(id_delete)
        return deleted



