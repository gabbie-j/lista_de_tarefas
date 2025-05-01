def adicionar_tarefa(lista_de_tarefas, tarefa):
# Adiciona tarefas a uma nova lista
  lista_de_tarefas.append(tarefa)
  print('\033[32mTarefa adicionada com sucesso!\033[0m')
  return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
# Exibe tarefas de uma lista preexistente 
  print('\n')
  print('=' * 50)
  print(f"{' ' * 17}LISTA DE TAREFAS{' ' * 20}")
  print('-' * 50)
  n = 1
  for tarefa in lista_de_tarefas:
    print(f'{n} - {tarefa}')
    n += 1
  print('-' * 50)

def exibir_menu():
# Exibe menu com opções para usuárie escolher
  print('-' * 50)
  print("\033[0mEscolha uma opção:\n"
    "1 - Inserir nova tarefa\n"
    "2 - Listar tarefas\n"
    "3 - Deletar tarefa\n"
    "4 - sair\033[0m"
  )
  print('-' * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
# Deleta tarefas de uma lista de tarefas preexistente a partir do número dela
  lista_de_tarefas.pop(tarefa - 1)
  return lista_de_tarefas

# Inicialização de variáveis
lista_de_tarefas = []
continuar = True

# Cabeçalho do programa
print('\033[0m-\033[0m' * 50)
print(f"{' ' * 10}\033[0m\033[33mBem vinde à sua LISTA DE TAREFAS\033[33m\033[0m{' ' * 20}")
print('\033[0m-\033[0m' * 50)

# Loop principal
while continuar:
  exibir_menu()
  opcao = input('\033[0m\033[34mInsira o número da opção desejada:\033[34m\033[0m ')
  if opcao == '1':
    tarefa = input('Insira uma nova tarefa: ')
    lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
  elif opcao == '2':
    listar_tarefas(lista_de_tarefas)
  elif opcao == '3':
# A validação verifica se o valor é numérico, se é maior que o valor da lista e se é menor ou igual a zero    
    tarefa = (input('Insira o número da tarefa que deseja deletar: '))
    if not tarefa.isnumeric():
      print('\033[31mNúmero inválido! Tente novamente.\033[0m')
    elif int(tarefa) > len(lista_de_tarefas) or int(tarefa) <= 0:
      print('\033[31mNúmero inválido! Tente novamente.\033[0m')
    else:
      deletar_tarefa(lista_de_tarefas, int(tarefa))
  elif opcao == '4':
    continuar = False
    print('\033[33mAté Logo!\033[33m\033[0m')
  else:
    print('\033[31mOpção inválida! Por favor, tente novamente.\033[0m')
  print('\n')