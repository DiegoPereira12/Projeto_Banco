from cliente import Cliente

class Conta(object):

   def __init__(self, numero, saldo, limite):
        self.numero = numero
        self.__saldo = 0.0
        self.__limite = 100.0
        
    def retorna_numero(self):
        return self.numero

    def retorna_cliente(self):
        return self.cliente
    
    @property
    def retorna_saldo(self):
        return self.__saldo
    
    @property
    def retorna_limite(self):
        return self.__limite




    