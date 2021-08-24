from modulo.cliente import Cliente

class Conta():

    codigo = 1001

    def __init__(self, nome, cpf, data_nascimento):
        self.numero = Conta.codigo
        super().__init__(nome, cpf, data_nascimento)
        self.__saldo = 0.0
        self.__limite = 100.0
        Conta.codigo += 1
        
    def retorna_numero(self):
        return self.numero
    
    @property
    def retorna_saldo(self):
        return self.__saldo
    
    @property
    def retorna_limite(self):
        return self.__limite
    
    def dados(self):
        print(f' O %s  tem o cpf %s é nasceu no dia %s é sua conta bancária %s com o saldo de %s' %(self.nome, self.__cpf, self.numero, self.__saldo))
    
    nome = Cliente('Diego')
    cpf = Cliente('0722451725')
    data_nascimento = Cliente('12071989')
    
