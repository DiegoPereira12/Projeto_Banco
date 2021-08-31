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

def efetuar_saque():
    if len(contas) > 0:
        numero = int(input('Digite o número da sua conta => '))

        conta: Conta = buscar_conta(numero)

        if conta:
            valor = float(input('Digite o valor do saque => '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrado uma conta com o número {numero}')
    
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    principal.menu()

def efetuar_deposito():
    if len(contas) > 0:
        numero = int(input('Digite o numero da sua conta => '))

        conta: Conta = buscar_conta(numero)

        if conta:
            valor = float(input("Digite o valor do depósito => "))

            conta.depositar(valor)
        else:
            print(f'Não foi  encontrado uma conta com o número {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    principal.menu()

def efetuar_transferencia():
    if len(contas) > 0:
        numero_origem = int(input('Digite o número de sua conta => '))

        conta_origem: Conta = buscar_conta(numero_origem)

        if conta_origem:
            numero_destino = int(input('Digite o número da conta de Destino => '))

            conta_destino: Conta = buscar_conta(numero_destino)

            if conta_destino:
                valor = float(input('Digite o valor da transferência => '))

                conta_origem.transferir(conta_destino, valor)
            else:
                (f'A conta de destino {numero_destino} não foi encontrada')
        else:
            (f' A sua conta de origem {numero_origem} não foi encontrada')
    else:
        ('Ainda não existem contas cadastradas')
    sleep(2)
    principal.menu()









def buscar_conta(numero: Conta):
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

principal.menu    
