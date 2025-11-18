from operacoesbd import *

def listarManifestacoes(conexao):
    consulta = 'select * from Manifestacoes;'
    manifestacoes = listarBancoDados(conexao, consulta)

    if len(manifestacoes) == 0:
        print("Nenhuma manifestação encontrada")

    else:
        print("Lista de Manifestações:")
        for i in range(len(manifestacoes)):
            print(str(i+1) + ')', manifestacoes[i][1])

def registrarManifestacoes(conexao):
    novaManifestacao = input('Digite a manifestação a ser registrada: ')

    consulta = 'insert into Manifestacoes (manifestacao) values(%s);'
    dados = [novaManifestacao]

    codigoNovaManifestacao = insertNoBancoDados(conexao, consulta, dados)
    print("Manifestação registrada com sucesso! O código é", codigoNovaManifestacao)

def pesquisarManifestacoes(conexao):
    codigoManifestacao = int(input("Digite o código da manifestação a ser consultada: "))

    consulta = 'select * from Manifestacoes where codigo = %s;'
    valores = [codigoManifestacao]

    manifestacoes = listarBancoDados(conexao, consulta, valores)

    if len(manifestacoes) > 0:
        print('Nome da Manifestação:', manifestacoes[0][1])

def removerManifestacoes(conexao):
    codigoManifestacao = int(input("Digite o código da manifestação a ser removida: "))

    consulta = 'delete from Manifestacoes where codigo = %s;'
    valores = [codigoManifestacao]

    manifestacoesRemovidas = excluirBancoDados(conexao, consulta, valores)

    if manifestacoesRemovidas == 0:
        print('Não existe manifestação para o código informado!')

    else:
        print('Manifestação removida com sucesso!')

def quantidadeManifestacoes(conexao):
    consulta = 'select count(*) from Manifestacoes;'
    manifestacoes = listarBancoDados(conexao, consulta)

    print('Atualmente temos', manifestacoes[0][0], 'manifestações(s).')