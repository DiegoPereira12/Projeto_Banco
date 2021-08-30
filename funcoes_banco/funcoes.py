from time import sleep
from modulo.cliente import Cliente
from modulo.conta import Conta
import principal


contas = []

def criar_conta():
    print('Informe os dados do cliente')

    nome = input('Digite o Nome do cliente => ')
    cpf = input('Digite o CPF do cliente => ')
    data_nascimento = input('Digite  a Data de Nascimento do cliente => ')

    cliente: Cliente = Cliente(nome, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Sua conta foi criada com sucesso')
    print('------------------')
    print(conta)
    print('------------------')
    sleep(2)
    principal.menu()


    