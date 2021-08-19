class Cliente(object):
    
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.__cpf = cpf
        self.data_nascimento = data_nascimento
      
    def retorna_nome(self):
        return self. nome
    
    def retorna_cpf(self):
        return self.__cpf
    
    def retorna_datanascimento(self):
        return self.data_nascimento
    