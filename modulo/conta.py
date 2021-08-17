from typing import NoReturn
from cliente import Cliente

class Conta(object):

    codigo: 1001

    def __init__(self, numero, cliente: Cliente, saldo, limite): 
        self.numero = numero
        self.cliente: Cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100.0
        Conta.codigo +=1

    def numero(self):
        return self.numero

    def cliente(self):
        return self.cliente
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite




    