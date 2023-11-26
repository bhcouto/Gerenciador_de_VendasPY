# Gerenciador_de_VendasPY
Este é um simples aplicativo de gerenciamento de vendas desenvolvido em Python usando a biblioteca Tkinter para a interface gráfica e MySQL Connector para interação com um banco de dados MySQL.

# Funcionalidades

## Limpar Tela
Método: limpa_tela()
Descrição: Limpa os campos de entrada na interface gráfica.

## Conectar ao Banco de Dados
Método: conecta_bd()
Descrição: Estabelece uma conexão com o banco de dados MySQL.

## Desconectar do Banco de Dados
Método: desconecta_bd()
Descrição: Encerra a conexão com o banco de dados MySQL.

## Criar Tabela no Banco de Dados
Método: criar_tabela()
Descrição: Cria a tabela 'vendas' no banco de dados, se ainda não existir.

## Adicionar Produto
Método: add_produto()
Descrição: Adiciona um novo produto à tabela 'vendas' no banco de dados.

## Selecionar Lista de Produtos
Método: select_lista()
Descrição: Atualiza a lista de produtos na interface gráfica.

## Duplo Clique na Lista para Editar
Método: OnDoubleClick()
Descrição: Permite a edição de um produto ao fazer um duplo clique na lista.

## Excluir Produto
Método: delete_produto()
Descrição: Exclui um produto da tabela 'vendas' no banco de dados.

## Alterar Produto
Método: alterar_produto()
Descrição: Altera as informações de um produto na tabela 'vendas' no banco de dados.

## Buscar Produto
Método: buscar_produto()
Descrição: Busca produtos na tabela 'vendas' com base no nome.
Interface Gráfica
A interface gráfica consiste em dois frames:

Frame 1: Contém campos de entrada para ID, nome do produto, valor e descrição, além de botões para limpar, buscar, adicionar, alterar e excluir produtos.

Frame 2: Exibe uma lista de produtos com colunas para ID, produto, valor e descrição. Permite seleção dupla para edição.


## Utilização

1. Certifique-se de ter o Python instalado no seu sistema.

2. Instale as dependências usando o seguinte comando no terminal:

   ```bash
   pip install -r requirements.txt

3. Coloque seu acesso na função ConectaBd()
   def conecta_bd(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="SeuUsuario",
            password="SuaSenha",
            database="SeuBancodedados"
        )  





