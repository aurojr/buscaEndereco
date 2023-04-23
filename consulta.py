import pandas as pd
import requests
from termcolor import colored


def buscar_por_cep(cep):
    # trata o cep
    cep = cep.replace(".", "").replace("-", "")

    while cep.isnumeric() == False or len(cep) < 8:
        # looping que verifica se o CEP é numérico e possui 8 digitos
        print("CEP Inválido")
        cep = input("Insira o CEP: ")
        cep = cep.replace(".", "").replace("-", "")

    else:
        try:
            # verifica se o CEP é valido - minimo 8 digitos
            endpoint = f"https://viacep.com.br/ws/{cep}/json/"
            requisicao = requests.get(endpoint)
            dic_end = requisicao.json()

            endereco = dic_end["logradouro"]
            bairro = dic_end["bairro"]
            cidade = dic_end["localidade"]
            uf = dic_end["uf"]
            print()

            print(
                f"\033[92mCEP: {cep}\nEndereço: {endereco}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {uf}\033[m"
            )
            print()
            return dic_end
        except:
            print()
            print("CEP não encontrado, tente novamente")
            print()


# dicionario_cep = buscar_por_cep()


def buscar_por_end(uf, cidade, endereco):
    # parametros obrigatórios para busca por endereço

    try:
        endpoint = f"https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/"
        requisicao = requests.get(endpoint)
        requisicao = requisicao.json()

        tabela = pd.DataFrame(requisicao)
        tabela = tabela.rename(
            columns={
                "cep": "CEP",
                "logradouro": "Logradouro",
                "localidade": "Localidade",
                "bairro": "Bairro",
                "uf": "UF",
            }
        )
        tabela = colored(
            tabela[["CEP", "Logradouro", "Bairro", "Localidade", "UF"]], "green"
        )

        print("Foram encontrados {} resultados".format(len(tabela)))
        print()
        print(tabela)
        return tabela
    except:
        print("Endereço não encontrado, tente novamente ")
        print()
