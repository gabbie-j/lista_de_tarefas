# lista_de_tarefas

Este é um programa simples em Python que permite adicionar, listar e excluir tarefas de uma lista, tudo pelo terminal.

Funcionalidades
Adicionar novas tarefas à lista

Listar todas as tarefas registradas

Deletar uma tarefa existente

Sair do programa

Como Usar
Execute o programa.

Escolha uma opção do menu:

1 - Inserir nova tarefa

2 - Listar tarefas

3 - Deletar tarefa

4 - Sair

Siga as instruções de cada opção para gerenciar sua lista de tarefas.

Estrutura do Código
adicionar_tarefa(lista_de_tarefas, tarefa): Adiciona uma nova tarefa à lista.

listar_tarefas(lista_de_tarefas): Exibe todas as tarefas atuais da lista.

exibir_menu(): Mostra o menu de opções ao usuário.

deletar_tarefa(lista_de_tarefas, tarefa): Remove uma tarefa da lista com base em seu número.

Loop principal que mantém o programa em execução até o usuário decidir sair (opção 4).

Validações
Na exclusão de tarefas:

Verifica se o valor digitado é numérico.

Verifica se o número corresponde a uma tarefa existente (não é menor ou igual a zero e não excede o número de tarefas).

Estilização
O programa utiliza códigos de cor ANSI para deixar o terminal mais amigável:

Verde para sucesso

Vermelho para erros

Amarelo para mensagens de despedida

Azul para entrada de dados
