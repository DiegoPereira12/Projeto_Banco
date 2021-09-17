from modulo.cliente import Cliente

class Conta:

    codigo = 1001

    def __init__(self: object, cliente: Cliente) -> None:
       self.__numero:int = Conta.codigo
       self.__cliente: Cliente = cliente
       self.__saldo: float = 0.0
       self.__limite: float = 100.0
       self.__saldo_total: float = self.calcula_saldo_total
       Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Numero da conta: {self.numero} \nCliente: {self.cliente.nome} ' \
            f'\nSaldo Total: {(self.saldo_total)}'
    
    @property
    def retorna_numero(self: object) -> int:
        return self.__numero
    
    @property
    def retorna_cliente(self: object) -> Cliente:
        return self.__cliente
    
    @property
    def retorna_saldo(self: object) -> float:
        self.__saldo
    
    @retorna_saldo.setter
    def retorna_saldo(self: object, valor: float) -> None:
        self.__saldo = valor
    
    @property
    def retorna_limite(self: object) -> float:
        return self.__limite
    
    @retorna_limite.setter
    def retorna_limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def retorna_saldo_total(self:object) -> float:
        return self.__saldo_total
    
    @retorna_saldo_total.setter
    def retorna_saldo_total(self:object, valor: float) -> None:
        self.__saldo_total = valor
    
    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!')
        else:
            print('Erro ao efetuar depósito. Tente novamente')

    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso')
        else:
            print('Saque não realizado. Tente novamente')

    def transferir(self: object, destino: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            print('Transferência realizada com sucesso.')
        else:
            print('Transferência não realizada. Tente novamente')
