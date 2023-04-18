from menu import apontar_funcoes, escolher_opcao, menu

opcao = ''
while opcao != '3':
    menu()
    opcao = input('Escolha usa opção: ')
    valor = escolher_opcao(opcao)
    apontar_funcoes(valor)
    print()
