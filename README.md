<h1 align="center">Sprint 4 - Computational Thinking with Python</h1>

## Descrição do projeto
* Projeto desenvolvido em Pyhton para demonstrar funcionamento do aplicativo UrbanFlow. 
  <br>
* O UrbanFlow é uma ferramenta inovadora projetada para melhorar a experiência dos usuários de transporte público. Ele oferece uma série de recursos essenciais para ajudar os passageiros a acompanhar e otimizar suas viagens de ônibus de maneira conveniente e eficiente.

## Estrutura do Projeto
O projeto é composto por três arquivos principais:

* main.py: Contém o código principal do programa, responsável pela interação com o usuário, cadastro, login e execução das principais funcionalidades.

* funcoes.py: Agrupa diversas funções utilitárias utilizadas no programa principal, como validação de opções, login, exibição de dicionários e manipulação de favoritos.

* dics_e_listas.py: Armazena as informações sobre ônibus, destinos e o modelo de dados do usuário.

## Funcionalidades

### 1. Cadastro e Login
* Ao iniciar o programa, o usuário é solicitado a fornecer informações pessoais, como nome, email, senha e endereço. Após o cadastro, é necessário fazer o login para acessar as funcionalidades principais.

### 2. Opções Principais
* Após o login, o usuário pode escolher entre as seguintes opções:

* Exibir todos os ônibus disponíveis agora (Opção 1): Mostra uma tabela com informações sobre todos os ônibus disponíveis, incluindo número, nome, lotação e tempo de chegada.

* Escolher um destino e ver os melhores ônibus para chegar nele (Opção 2): Permite ao usuário escolher entre três destinos predefinidos e exibe os ônibus mais adequados para cada destino.

* Adicionar um ônibus a minha lista de favoritos (Opção 3): Permite ao usuário adicionar um ônibus à sua lista de favoritos, que é armazenada localmente.

* Ver meus ônibus favoritos (Opção 4): Exibe a lista de ônibus favoritos salvos pelo usuário.

* Sair (Opção 5): Encerra o programa.

### 3. Funcionalidades Adicionais
* Validação de Opções (forca_opcao): Garante que o usuário selecione uma opção válida em qualquer menu.

* Login com Tentativas (login): Fornece três tentativas para o usuário realizar o login corretamente.

* Manipulação de Favoritos (carregar_favoritos, salvar_favoritos, add_fav, verificar_fav): Permite ao usuário adicionar, visualizar e salvar ônibus favoritos.

## Observações
* As informações dos ônibus e destinos são pré-definidas em 'dics_e_listas.py' e podem ser modificadas conforme necessário.

* As informações dos usuários são temporariamente armazenadas em um dicionário e não persistem após a execução do programa.

* A lista de favoritos é salva localmente em um arquivo JSON chamado 'favoritos.json'.

## Requisitos

* Python 3.9
  <br>
* PyCharm IDE

## Dependências

* Biblioteca Pandas
* Biblioteca JSON

## Melhorias Futuras
* Implementar persistência de dados de usuários utilizando um banco de dados.

* Expandir as opções de destinos e permitir que o usuário insira destinos personalizados.

* Aprimorar a interface de usuário para tornar a experiência mais amigável.

* Adicionar funcionalidades como busca de ônibus por nome, filtro por lotação, etc.

## Colaboradores
<table>
  <tr>
    <td align="center">
        <sub>
          <b>Enzo Luiz Goulart - RM99666</b>
          <br>
        </sub>
        <sub>
          <b>Natan Eguchi dos Santos - RM98720</b>
          <br>
        </sub>
        <sub>
          <b>Kayky Paschoal Ribeiro - RM99929</b>
          <br>
        </sub>
        <sub>
          <b>Gustavo Henrique Santos Bonfim - RM98864</b>
          <br>
        </sub>
        <sub>
          <b>Lucas Yuji Farias Umada - RM99757 </b>
          <br>
        </sub>
    </td>
  </tr>
</table>


## Status do projeto
Em desenvolvimento
