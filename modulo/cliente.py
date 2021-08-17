class Cliente(object):
    
    contador: int = 0

    def __init__(self, nome, cpf, data_nascimento):
        self.codigo = Cliente.contador
        self.nome  = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento
        Cliente.contador += 1

    def codigo(self):
        return self.codigo

    def nome(self):
        return self.nome

    @property
    def cpf(self):
        return self.__cpf

    def dat_nascimento(self):
        return self.data_nascimento