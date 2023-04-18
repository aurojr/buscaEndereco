from lista_menu import lista
from consulta import buscar_por_cep, buscar_por_end
from save_file import save_file, save_xls
import sys
import os
import time


def menu():
    # Formata o menu
    string = '#'
    barra = string * 42
    titulo = ' MENU PRINCIPAL '
    titulo_principal = titulo.center(42, '#')

    c = 1
    print(titulo_principal)
    for item in lista:
        print('\033[33m[{}]\033[m - \033[34m{}\033[m'.format(c, item))
        c += 1
    print(barra)
    print()


def apontar_funcoes(valor):
    if valor == '1':
        cep = input('Insira o CEP: ')
        buscar_por_cep(cep)

    elif valor == '2':
        uf = input('Insira o Estado: ')  # minimo dois caracteres
        while uf.isalpha() == False or len(uf) < 2 or len(uf) > 2:  # != 2
            print('Insira a silgla do Estado - minimo 2 caracteres')
            uf = input('Insira o Estado: ')

        cidade = input('Insira a Cidade: ')  # minimo dois caracteres
        while len(cidade) < 2 or not cidade.isalpha():
            print('Insira o nome da cidade - Minimo 2 caracteres')
            cidade = input('Insira a Cidade: ')

        
        endereco = input('Insira o Endereço ')  # minimo tres caracateres
        while len(endereco) <= 2:
            print('Endereço deve conter mais de 3 caracteres')
            endereco = input('Insira o Endereço ')
            print()
        buscar_por_end(uf, cidade, endereco)

    elif valor == '3':
        print('Obrigado! Saindo do Sistema...')
        time.sleep(1)
        os.system('cls')
        sys.exit()


def escolher_opcao(opt):
    return opt
