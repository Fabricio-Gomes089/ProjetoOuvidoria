
from ouvidoria import *
from operacoesbd import *

conexao = criarConexao('127.0.0.1','root','@Dragonballz123','projeto_ouvidoria')

opcao = -1
manifestacoes = []

while opcao != 7:
    print('\n   MENU DE MANIFESTAÇÕES')
    print('1) Listar Manifestações')
    print('2) Registrar Manifestação')
    print('3) Procurar Manifestação pelo tipo')
    print('4) Procurar Manifestação pelo código')
    print('5) Remover Manifestação')
    print('6) Quantidade de Manifestações')
    print('7) Sair')

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        listarManifestacoes(conexao)

    elif opcao == 2:
        adicionarManifestacao(conexao)

    elif opcao == 3:
        pesquisarManifestacoesTipo(conexao)

    elif opcao == 4:
        pesquisarManifestacoesCodigo(conexao)

    elif opcao == 5:
        removerManifestacao(conexao)

    elif opcao == 6:
        quantidadeManifestacao(conexao)

    elif opcao != 7:
        print('Opção inválida!')

print('Obrigado por usar o App da Ouvidoria!')

encerrarConexao(conexao)