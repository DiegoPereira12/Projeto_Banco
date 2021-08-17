from cliente import Cliente

class Conta(object):

    codigo: 1001

    def __init__(self, numero, cliente: Cliente, saldo, limite): 
        self.numero = numero
        self.cliente: Cliente = cliente
        self.__saldo = 0.0
        self.__limite = 100.0
        Conta.codigo +=1
    


    