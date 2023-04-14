import requests
import pandas as pd


def buscar_por_cep():
    cep = input('Insira o CEP: ')
    # trata o cep
    cep = cep.replace('.', '').replace('-', '')

    while cep.isnumeric() == False or len(cep) < 8:
        # looping que verifica se o CEP é numérico e possui 8 digitos
        print('CEP Inválido')
        cep = input('Insira o CEP: ')
        cep = cep.replace('.', '').replace('-', '')

    else:
        try:
            # verifica se o CEP é valido - minimo 8 digitos
            endpoint = f'https://viacep.com.br/ws/{cep}/json/'
            requisicao = requests.get(endpoint)
            dic_end = requisicao.json()

            endereco = dic_end['logradouro']
            bairro = dic_end['bairro']
            cidade = dic_end['localidade']
            uf = dic_end['uf']
            print()

            print(
                f'CEP: {cep}\nEndereço: {endereco}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {uf}')

            return dic_end
        except:
            print('CEP não encontrado, tente novamente')


# dicionario_cep = buscar_por_cep()


def buscar_por_end():
    # parametros obrigatórios para busca por endereço

    uf = input('Insira o Estado: ')  # minimo dois caracteres

    while uf.isalpha() == False or len(uf) < 2 or len(uf) > 2:
        print('Insira a silgla do Estado')
        uf = input('Insira o Estado: ')

    cidade = input('Insira a Cidade: ')  # minimo dois caracteres

    while cidade.isalpha() == False and len(cidade) < 2:
        print('Insira o nome da cidade - Minimo 2 caracteres')
        cidade = input('Insira a Cidade: ')

    endereco = input('Insira o Endereço ')  # minimo tres caracateres
    while len(endereco) < 2:
        print('Endereço deve conter mais de 3 caracteres')
        endereco = input('Insira o Endereço ')

    print()
    print()
    try:
        endpoint = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'
        requisicao = requests.get(endpoint)
        requisicao = requisicao.json()

        tabela = pd.DataFrame(requisicao)
        tabela = tabela[['cep', 'logradouro', 'bairro', 'localidade', 'uf']]

        print('Foram encontrados {} resultados'.format(len(tabela)))
        print()
        print(tabela)
        return tabela
    except:
        print('Endereço não encontrado, tente novamente ')
