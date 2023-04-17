from menu import menu, escolher_opcao, apontar_funcoes

opcao = ''
while opcao != '3':
    menu()
    opcao = input('Escolha usa opção: ')
    valor = escolher_opcao(opcao)
    apontar_funcoes(valor)
    print()
