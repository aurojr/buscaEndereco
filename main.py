from menu import menu, escolher_opcao, apontar_funcoes


def main():
    opcao = ''
    while opcao != '3':
        menu()
        opcao = input('Escolha usa opção: ')
        valor = escolher_opcao(opcao)
        apontar_funcoes(valor)
        print()


if __name__ == '__main__':
    main()
