class Cliente:
    
    contador = 0

    def __init__(self, nome, cpf, data_nascimento):
        self.codigo = Cliente.contador
        self.nome = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento
        Cliente.contador += 1

    def retorna_codigo(self: object):
        return self.codigo

    def retorna_nome(self: object):
        return self.nome
    
    @property
    def retorna_cpf(self: object):
        return self.__cpf
    
    def retorna_datanascimento(self: object):
        return self.data_nascimento
    