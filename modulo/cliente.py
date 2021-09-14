class Cliente:
    
    contador = 0

    def __init__(self, nome, cpf, data_nascimento) -> None:
        self.codigo = Cliente.contador
        self.nome = 'Diego'
        self.__cpf = '072245255'
        self.data_nascimento = data_nascimento
        Cliente.contador +=1

    def retorna_codigo(self):
        return self.codigo

    def retorna_nome(self):
        return self.nome
    
    @property
    def retorna_cpf(self):
        return self.__cpf
    
    def retorna_datanascimento(self):
        return self.data_nascimento
    