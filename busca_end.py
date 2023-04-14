import requests
import json
import pandas as pd
from consulta import buscar_por_cep, buscar_por_end

# Escolha o tipo de busca

opcao = input('[1] Busca por CEP\n[2] Busca por Endereço\n\n')

if opcao == '1':
    buscar_por_cep()
else:
    buscar_por_end()
