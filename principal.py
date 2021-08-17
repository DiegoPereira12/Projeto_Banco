from modulo.cliente import Cliente
from modulo.conta import Conta

contas = []

def menu():
    print('========== DIBANCO ==========')
    print('Selecione uma opçao no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar deposito')
    print('4 - Efetuar tranferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao = input("=>")

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito
    elif opcao == 4:
        efetuar_tranferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre ao DIBANCO')
        exit()
    else:
        print('Opçao invalida')                                 
