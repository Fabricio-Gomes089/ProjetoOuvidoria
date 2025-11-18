# 📄 Sistema de Gerenciamento de Manifestações

Este projeto contém um conjunto de funções em Python para gerenciamento
básico de manifestações registradas em um banco de dados. As operações
incluem listar, registrar, pesquisar, remover e contar registros.\
O código utiliza funções auxiliares importadas do módulo `operacoesbd`,
que encapsulam operações de acesso ao banco de dados.

## 📌 Pré-requisitos

Para que este código funcione corretamente, é necessário:

-   Um banco de dados contendo a tabela **Manifestacoes** com as
    colunas:
    -   `codigo` -- Identificador único da manifestação
        (auto-incremento).
    -   `manifestacao` -- Texto da manifestação registrada.
-   O módulo `operacoesbd` implementado com funções como:
    -   `listarBancoDados(conexao, consulta, valores=None)`
    -   `insertNoBancoDados(conexao, consulta, valores)`
    -   `excluirBancoDados(conexao, consulta, valores)`
-   Um objeto **conexao** conectado ao banco de dados.

## 📚 Funções Disponíveis

### 🔎 listarManifestacoes(conexao)

Lista todas as manifestações registradas.

-   Executa: `SELECT * FROM Manifestacoes;`
-   Exibe mensagem se não houver registros.
-   Caso existam, imprime cada manifestação numerada.

### 📝 registrarManifestacoes(conexao)

Cadastra uma nova manifestação informada pelo usuário.

-   Solicita o texto da manifestação.

-   Insere no banco com:

    ``` sql
    INSERT INTO Manifestacoes (manifestacao) VALUES (%s);
    ```

-   Exibe o código gerado para a nova manifestação.

### 🔍 pesquisarManifestacoes(conexao)

Pesquisa uma manifestação pelo seu **código**.

-   Solicita o código ao usuário.

-   Executa:

    ``` sql
    SELECT * FROM Manifestacoes WHERE codigo = %s;
    ```

-   Caso encontrada, mostra o texto correspondente.

### ❌ removerManifestacoes(conexao)

Remove uma manifestação com base no código informado.

-   Solicita o código ao usuário.

-   Executa:

    ``` sql
    DELETE FROM Manifestacoes WHERE codigo = %s;
    ```

-   Caso nenhum registro seja removido, informa que o código não existe.

-   Caso contrário, confirma a exclusão.

### 🔢 quantidadeManifestacoes(conexao)

Mostra o número total de manifestações cadastradas.

-   Executa:

    ``` sql
    SELECT COUNT(*) FROM Manifestacoes;
    ```

-   Exibe o total encontrado.

## ▶️ Exemplo de Uso

Essas funções podem ser chamadas dentro de um sistema com menu, como:

-   Listar → `listarManifestacoes(conexao)`
-   Cadastrar → `registrarManifestacoes(conexao)`
-   Pesquisar → `pesquisarManifestacoes(conexao)`
-   Remover → `removerManifestacoes(conexao)`
-   Contar → `quantidadeManifestacoes(conexao)`

## 🧩 Observações

-   O código não faz tratamento de exceções.
-   Recomenda-se adicionar validações e captura de erros para uso em
    produção.
