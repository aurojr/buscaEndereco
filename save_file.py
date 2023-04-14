from consulta import buscar_por_cep, buscar_por_end
import pandas as pd


def save_file():
    try:
        df = pd.DataFrame.from_dict(dic_impressao_cep)
        df.to_csv(r'arquivo.csv', index=False, header=True)
    except:
        print('Não foi possível salvar o arquivo')


def save_xls():
    try:
        df = pd.DataFrame.from_dict(dic_impressao_end)
        df.to_excel(r'arquivo.xls', index=False, header=True)
    except:
        print('Não foi possível salvar o arquivo')
