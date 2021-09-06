from time import sleep
import funcoes_banco.funcoes

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
        funcoes_banco.funcoes.criar_conta()
    elif opcao == 2:
        funcoes_banco.funcoes.efetuar_saque()
    elif opcao == 3:
        funcoes_banco.funcoes.efetuar_deposito()
    elif opcao == 4:
        funcoes_banco.funcoes.efetuar_transferencia()
    elif opcao == 5:
        funcoes_banco.funcoes.listar_contas()
    elif opcao == 6:
        print('Sessão encerrada')
        sleep(2)
        exit()
    else:
        print('Opção inválida')
    
    sleep(2)
    menu()