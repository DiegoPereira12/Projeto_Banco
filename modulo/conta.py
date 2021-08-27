from modulo.cliente import Cliente

class Conta(Cliente):

    codigo = 1001

    def __init__(self, nome, cpf, data_nascimento, saldo_total):
        self.numero = Conta.codigo
        super().__init__(nome, cpf, data_nascimento)
        self.__saldo = 0.0
        self.__limite = 100.0
        self.__saldo_total = self._calcula_saldo_total
        Conta.codigo += 1
        
    def retorna_numero(self):
        return self.numero
    
    def retorna_cliente(self):
        return super(Cliente)
    
    @property
    def retorna_saldo(self):
        return self.__saldo
    
    @retorna_saldo.setter
    def retorna_saldo(self, valor):
        self.__saldo = valor
    
    @property
    def retorna_limite(self):
        return self.__limite
    
    @retorna_limite.setter
    def retorna_limite(self, valor):
        self.__limite = valor
    
    @property
    def retorna_saldo_total(self):
        return self.__saldo_total
    
    @retorna_saldo_total.setter
    def retorna_saldo_total (self, valor):
        self.__saldo_total= valor
    
    @property
    def _calcula_saldo_total(self):
        return self.__saldo + self.__limite

    def depositar(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
            self.__saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!!!')
        else:
            print('Erro ao efetuar depósito. Tente novamente')


    

