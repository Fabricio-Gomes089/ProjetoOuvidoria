#Grupo:
#Samuel Herbert Félix Rodrigues 
#Fabricio Gomes Candido Filho
#Iago Yehudi Rabi Pereira Da Silva
#João Matheus Eleotério Soares

from ouvidoria import *
from operacoesbd import *

conexao = criarConexao(endereco = 'localhost', usuario ='root', senha ='@Dragonballz123', bancodedados='projeto_ouvidoria')

opcao = -1
manifestacoes = []

while opcao != 6:
    print('\n   MENU DE MANIFESTAÇÕES')
    print('1) Listar Manifestações')
    print('2) Registrar Manifestação')
    print('3) Procurar Manifestação')
    print('4) Remover Manifestação')
    print('5) Quantidade de Manifestações')
    print('6) Sair')

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        listarManifestacoes(conexao)

    elif opcao == 2:
        registrarManifestacoes(conexao)

    elif opcao == 3:
        pesquisarManifestacoes(conexao)

    elif opcao == 4:
        removerManifestacoes(conexao)

    elif opcao == 5:
        quantidadeManifestacoes(conexao)

    elif opcao != 6:
        print('Opção inválida!')

encerrarConexao(conexao)

print('Obrigado por usar o app!')