class Cliente:
    
    contador = 0

    def __init__(self, nome, cpf, data_nascimento):
        self.codigo: int = Cliente.contador
        self.nome: str = nome
        self.__cpf: str = cpf
        self.data_nascimento: str = data_nascimento
        Cliente.contador += 1

    def retorna_codigo(self: object) -> str:
        return self.codigo

    def retorna_nome(self: object) -> str:
        return self.nome
    
    @property
    def retorna_cpf(self: object) -> str:
        return self.__cpf
    
    def retorna_datanascimento(self: object) -> str:
        return self.data_nascimento
    