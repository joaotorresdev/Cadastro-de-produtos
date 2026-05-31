# Cadastro de Produtos

Este é um projeto inicial em Python desenvolvido para praticar conceitos de estruturas de repetição, condicionais, listas e manipulação de arquivos de texto (`.txt`) para persistência, leitura e remoção de dados.

![Execução do Programa](https://github.com/joaotorresdev/Cadastro-de-produtos/blob/main/printcadasprodutos.png)

## 🚀 Sobre o Projeto

O script simula um sistema de gestão de stock com um menu interativo no terminal. Ele permite ao utilizador registar novos produtos (guardando o código, nome, preço e quantidade diretamente num arquivo de texto local), listar todos os itens guardados de forma organizada e excluir um registo com base na sua linha correspondente no arquivo.

## 🛠️ Tecnologias Utilizadas

* Python 3

## 💻 Como Funciona o Código

O fluxo do programa é estruturado em torno de um laço de repetição (`while`) que mantém o menu ativo até que a opção de saída seja escolhida. Está dividido em quatro etapas principais:

1. **Menu Interativo:** Exibe as opções de controlo no terminal e captura a opção selecionada pelo utilizador.
2. **Registo de Produtos (Opção 1):** Solicita as informações do produto. Estes dados são concatenados e gravados de forma permanente no arquivo `cad_produtos.txt` utilizando o modo de anexação (`"a"`).
3. **Listagem de Produtos (Opção 2):** Abre o arquivo de texto no modo de leitura (`"r"`), percorre cada linha existente, divide os dados pelas vírgulas e exibe as informações estruturadas com tabulações (`\t`) no terminal.
4. **Exclusão de Produtos (Opção 3):** Lê todas as linhas do arquivo e armazena-as temporariamente numa lista. O programa solicita o número da linha a remover, elimina esse elemento utilizando o método `pop()` e reescreve o arquivo atualizado utilizando o modo de gravação (`"w"`).
