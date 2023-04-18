from menu import menu, escolher_opcao, apontar_funcoes


def main():
    opcao = ''
    while opcao != '3':
        menu()
        opcao = input('Escolha usa opção: ')
        apontar_funcoes(opcao)
        print()


if __name__ == '__main__':
    main()
