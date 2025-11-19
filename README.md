# 📄 Sistema de Gerenciamento de Manifestações

Este projeto implementa um conjunto de funções em Python para gerenciar manifestações registradas em um banco de dados. As funcionalidades incluem cadastrar, listar, pesquisar, remover e contar manifestações, com suporte a diferentes tipos: **Reclamação**, **Elogio** e **Sugestão**.

As funções utilizam comandos SQL e dependem de funções de acesso ao banco de dados fornecidas por um módulo externo, como:

- listarBancoDados(conexao, consulta, valores=None)
- insertNoBancoDados(conexao, consulta, valores)
- excluirBancoDados(conexao, consulta, valores)

## 📌 Requisitos

Para utilizar o sistema, é necessário:

- Banco de dados contendo a tabela Manifestacoes, com colunas como:
  - codigo
  - descricao
  - autor
  - tipo
- Conexão ativa com o banco (objeto conexao)
- Implementação das funções de banco no módulo externo

## 📚 Descrição das Funções

### 🔢 quantidadeManifestacao(conexao)
Exibe o total de manifestações cadastradas no banco.

### ❌ removerManifestacao(conexao)
Remove uma manifestação a partir do seu código.

### 🔍 pesquisarManifestacoesCodigo(conexao)
Pesquisa uma manifestação específica pelo código.

### 🔎 pesquisarManifestacoesTipo(conexao)
Pesquisa manifestações filtrando por tipo (Reclamação, Elogio ou Sugestão).

### 📝 adicionarManifestacao(conexao)
Adiciona uma nova manifestação ao banco.

### 📋 listarManifestacoes(conexao)
Lista todas as manifestações cadastradas.

## 🧩 Observações Importantes
- O sistema depende de funções externas para acesso ao banco.
- É recomendável adicionar validação e tratamento de erros.
