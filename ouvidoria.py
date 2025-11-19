import os
from operacoesbd import *


def quantidadeManifestacao(conexao):

    consulta = 'select count(*) from Manifestacoes;'
    manifestacoes = listarBancoDados(conexao, consulta)

    print('Atualmente temos', manifestacoes[0][0], 'manifestação(ões).')


def removerManifestacao(conexao):

    codigoManifestacao = int(input("Digite o código da manifestação a ser removida: "))

    consulta = 'delete from Manifestacoes where codigo = %s;'
    valores = [codigoManifestacao]

    manifestacoesRemovidas = excluirBancoDados(conexao, consulta, valores)

    if manifestacoesRemovidas == 0:
        print('Não existe manifestação para o código informado!')

    else:
        print('Manifestação removida com sucesso!')

def pesquisarManifestacoesCodigo(conexao):
    codigoManifestacao = int(input('Digite o código da manifestação a ser pesquisada: '))

    consulta = 'select * from Manifestacoes where codigo = %s'
    dados = [codigoManifestacao]
    manifestacoes = listarBancoDados(conexao, consulta, dados)

    for item in manifestacoes:
        print(item[0], '-', item[1], '- autor:', item[2], '-', item[3])

def pesquisarManifestacoesTipo(conexao):

    print('1) Reclamação 2) Elogio 3) Sugestão')
    tipoManifestacao = int(input('Digite o código referente ao tipo de manifestação: '))

    if tipoManifestacao == 1:
        dados = ['Reclamação']

    elif tipoManifestacao == 2:
        dados = ['Elogio']

    elif tipoManifestacao == 3:
        dados = ['Sugestão']

    else:
        print('Código inválido')

    consulta = 'select * from Manifestacoes where tipo = %s'
    manifestacoes = listarBancoDados(conexao, consulta, dados)
    dados = [tipoManifestacao]

    for item in manifestacoes:
        print(item[0], '-', item[1], '- autor:', item[2], '-', item[3])


def adicionarManifestacao(conexao):

    novaDescricao = input('Digite a descrição da manifestação: ')
    novoAutor = input('Digite o nome do autor: ')

    print('1) Reclamação 2) Elogio 3) Sugestão')
    tipoManifestacao = int(input('Digite o código referente ao tipo da manifestação:: '))

    if tipoManifestacao == 1:
        tipo = 'Reclamação'

    elif tipoManifestacao == 2:
        tipo = ['Elogio']

    elif tipoManifestacao == 3:
        tipo = ['Sugestão']

    else:
        print('Código inválido! Digite apenas 1, 2 ou 3')

    consulta = 'insert into Manifestacoes (descricao, autor, tipo) values (%s, %s, %s);'
    dados = [novaDescricao, novoAutor, tipo]
    codigoNovaManifestacoes = insertNoBancoDados(conexao, consulta, dados)

    print('Manifestação registrada com sucesso! O código é:', codigoNovaManifestacoes)


def listarManifestacoes(conexao):

    consulta = 'select * from Manifestacoes;'
    manifestacoes = listarBancoDados(conexao, consulta)

    for item in manifestacoes:
        print(item[0], '-', item[1], '- autor:', item[2], '-', item[3])
