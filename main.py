from consulta import buscar_por_cep, buscar_por_end
from menu import menu, escolher_opcao, apontar_funcoes

valor = ''
while valor != '4':
    menu()
    valor = escolher_opcao()
    apontar_funcoes(valor)
else:
    print('Obrigado! Saindo do Sistema...')
    print()
