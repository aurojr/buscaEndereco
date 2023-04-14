# buscaEndereco
 
Criado um sistemas de buscas de endereço por CEP ou por localidade através de Cidade e Estado.

Main.py
Chama as funções de Menu, seleção de opções e as funcionalidades de consulta, salvar arquivo em excel e sair de sistema
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Menu.py
Formata o menu permitindo maior facilidade e visualização das opções das funcções para o usuário:

def menu > Puxa a lista de menus do arquivo Lista_Menus

def_escolher_opcao >> Retorna o valor da opção selecionado pelo usuário

def apontar_funcoes >> Recolhe a opção escolhida pelo o usuário e de acordo com o valor chama a função selecionada. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Consulta.py

Contém as funções de busca por CEP e busca de endereço:

def_buscar_por_cep >> recebe o valor do cep como string, com o tratamento de retirar '.' (ponto) ou '-' (traço). Verifica após o tratamento
se o o mesmo possui oito digitos numericos. Após essa validação, é chamada a API de busca por CEP

def_buscar_por_endereço >> recebe as variáveis obrigatórias para busca: Estado e Cidade [onde é necessário ter no minimo dois caracateres e não ser valores numéricos] e o Endereço [necessário ter o menos 3 caracteres]. Feita essas validações ainda no input de cada uma delas, é feita uma requisição na API de busca de endereço. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Lista Menu.py
Contém as opções que aparecem no menu no formato lista, facilitando a manutenção, caso seja necessário remover/adicionar alguma opção.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Save File.py
Função para salvar o resultado da(s) busca(s) em um arquivo texto/planilha.  - EM CONSTRUÇÃO
