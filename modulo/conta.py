from modulo.cliente import Cliente

class Conta:

    codigo = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.numero = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100.0
        self.__saldo_total = self._calcula_saldo_total
        Conta.codigo += 1
    
    def __str__(self: object):
        return f'Numero da conta:{self.numero} \nCliente: {self.cliente.nome} ' \
               f'\nSaldo Total: {(self.saldo_total)}' 
        
    def retorna_numero(self: object):
        return self.numero
    
    @property
    def retorna_cliente(self: object) -> Cliente:
        return self.__cliente
    
    @property
    def retorna_saldo(self: object):
        return self.__saldo
    
    @retorna_saldo.setter
    def retorna_saldo(self: object, valor) -> None:
        self.__saldo = valor
    
    @property
    def retorna_limite(self: object):
        return self.__limite
    
    @retorna_limite.setter
    def retorna_limite(self: object, valor) -> None:
        self.__limite = valor
    
    @property
    def saldo_total(self: object):
        return self.__saldo_total
    
    @saldo_total.setter
    def saldo_total (self: object, valor) -> None:
        self.__saldo_total = valor
    
    @property
    def _calcula_saldo_total(self: object):
        return self.__saldo + self.__limite

    def depositar(self: object, valor) -> None:
        if valor > 0:
            self.__saldo = self.__saldo + valor
            self.__saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!!!')
        else:
            print('Erro ao efetuar depósito. Tente novamente')
    
    def sacar(self: object, valor) -> None:
        if 0 < valor <= self.__saldo_total:
            if self.__saldo >= valor:
                self.__saldo = self.__saldo - valor
                self.__saldo_total = self._calcula_saldo_total
            else:
                restante = self.__saldo - valor
                self.__limite = self.__limite + restante
                self.__saldo = 0
                self.__saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso')
        else:
            print('Saque não realizado. Tente novamente') 

    def transferir(self: object, valor, destino) -> None:
        if valor > 0 and self.__saldo_total >= valor:
            if self.__saldo >= valor:
                self.__saldo = self.__saldo - valor
                self.__saldo_total = self._calcula_saldo_total
                destino.__saldo = destino.__saldo + valor
                destino.__saldo_total = destino._calcula_saldo_total
            else:
                restante = self.__saldo  - valor
                self.__saldo = 0
                self.__limite = self.__limite + restante
                self.__saldo_total = self._calcula_saldo_total
                destino.__saldo = destino.__saldo + valor
                destino.__saldo_total = destino._calcula_saldo_total
            print('Transferência realizada com sucesso')
        else:
            print('Transferência não realizada. Tente novamente.')


