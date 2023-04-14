from menu import menu, escolher_opcao, apontar_funcoes

valor = ''
while valor != '4':
    menu()
    valor = escolher_opcao()
    apontar_funcoes(valor)
