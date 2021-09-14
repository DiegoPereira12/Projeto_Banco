from time import sleep

from modulo.cliente import Cliente
from modulo.conta import Conta

contas = []

def main():
    menu()

def menu():
    
    print('|========= DIBANCO =========|')
    print('Selecione uma opçao no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar deposito')
    print('4 - Efetuar tranferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')
    
    opcao = int(input('=> '))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
       efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Sessão encerrada')
        sleep(2)
        exit()
    else:
        print('Opção inválida')
    
    sleep(2)
    menu()

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
    menu()

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
    menu()

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
    menu()

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
    menu()

def listar_contas():
    if len(contas) > 0:
        print('Contas cadastradas')

        for conta in contas:
            print(conta)
            print('---------------------')
            sleep(2)
    else:
        print('Não existem contas cadastradas')
    sleep(2)
    menu()

def buscar_conta(numero: Conta):
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

if __name__ == '__main__':
    main()