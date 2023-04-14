def buscar_por_cep():
    cep = input('Insira o CEP: ')

    # trata o cep
    cep = cep.replace('.', '').replace('-', '')

    # verifica se o CEP é valido - minimo 8 digitos
    if len(cep) == 8:

        endpoint = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(endpoint)
        dic_end = requisicao.json()

        endereco = dic_end['logradouro']
        bairro = dic_end['bairro']
        cidade = dic_end['localidade']
        uf = dic_end['uf']
        print()

        print(
            f'O CEP {cep} pertence a >> {endereco} | Bairro: {bairro} | Cidade: {cidade}| Estado: {uf}')

    else:
        print('CEP Inválido')


def buscar_por_end():
    # parametros necessários para busca por endereço
    uf = input('Insira o Estado: ')
    cidade = input('Insira a Cidade: ')
    endereco = input('Insira o Endereço ')
    print()
    print()

    if len(uf) == 2 and len(cidade) > 2 and len(endereco) > 3:

        endpoint = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'
        requisicao = requests.get(endpoint)
        requisicao = requisicao.json()

        tabela = pd.DataFrame(requisicao)
        tabela = tabela[['cep', 'logradouro', 'bairro', 'localidade', 'uf']]

        print('Foram encontrados {} resultados'.format(len(tabela)))
        print()
        print(tabela)

    else:
        print('Dados do Logradouro devem conter mais de 2 caracteres')
