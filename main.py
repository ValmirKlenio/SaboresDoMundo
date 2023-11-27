# bibliotecas/imports
import csv

# listas/dicionarios
estoque = []
funcionarios = []
gestao = []
area_acesso = []
cardapios = []
fornecedores = []

# menu
def menu():
  print('''Escolha uma opção:
  [ 1 ] - Controle de Estoque
  [ 2 ] - Cadastro de Perfis de Acesso
  [ 3 ] - Gestão de Funcionários
  [ 4 ] - Monitoramento da Produção
  [ 5 ] - Pedidos a fornecedores
  [ 6 ] - Relatórios Gerenciais
  [ 7 ] - Sair/Encerrar''')

# modulo 1 - Samyra
def menu_mod1():
  print('''Escolha uma opção:
  1. Controle de Acesso
  2. Monitoramento do Estoque
  3. Alerta de Estoque
  4. Atualização do Estoque''')

def controle_acesso():
  nome = input('Nome: ')
  area = input('Área de Acesso: ')
  while nome and area not in area_acesso:
    print('ACESSO NEGADO! Seus dados não constam na area de acesso escolhida.')
    opc = input('Deseja criar um acesso para o funcionário? ')
    if opc == 'Ss':
      nome = input('Nome: ')
      area = input('Área de Acesso: ')
      area_acesso.append({'Nome': nome, 'Área de Acesso': area_acesso})
      print('ACESSO CRIADO!')
    else:
      break
  if nome and area in area_acesso:
    print('ACESSO PERMITIDO! Seus dados constam na area de acesso escolhida.')
  with open('acessos.csv', 'w', newline='') as acesso:
    escritor_csv = csv.writer(acesso)
    escritor_csv.writerows(area_acesso)
    print(escritor_csv)
  try:
    with open('acessos.csv', 'r') as acesso:
      leitor_csv = acesso.read()
      print(leitor_csv)
  except FileNotFoundError as erro:
    print(f'Erro: {erro}. O arquivo não foi encontrado.')
  area_acesso.append({'Nome': nome, 'Area de Acesso': area})
  print(area_acesso)

def monitora_estoque():
  # printar o arquivo csv para mostrar os ingredientes e suas quantidades
  for e in estoque:
    print('MONITORAMENTO DO ESTOQUE')
    print(e)
  try:
    with open('estoque.csv', 'r') as est:
      leitor_csv = est.read()
      print(leitor_csv)
  except FileNotFoundError as erro:
    print(f'Erro: {erro}. O arquivo não foi encontrado.')

def gera_alerta_estoque():
  # se pesquisar o ingrediente/produto e tiver menos que 3 quantidades, emitir um alerta de estoque baixo, mostrando que está abaixo do limite pré-estabelecido
  print('''Escolha uma opção:
  1. Pesquisar por ingediente
  2. Pesquisar por produtos''')
  opc = int(input('Opção: '))
  if opc == 1:
    ingrediente = input('Ingrediente: ')
    for i in estoque:
      ingrediente, quantidade = i
      print(i)
      if quantidade <= 3:
        print('ALERTA! Quantidade baixa no estoque!')
  elif opc == 2:
    produto = input('Produto: ')
    for p in estoque:
      produto, quantidade = p
      print(p)
      if quantidade <= 3:
        print('ALERTA! Quantidade baixa no estoque!')
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')

def atualiza_estoque():
  produto = input('Produto: ')
  quantidade = int('Quantidade para venda: ')
  if produto in estoque and estoque[produto] >= quantidade:
      estoque[produto] -= quantidade
      print(f"Entrega de {quantidade} unidades de {produto} realizada com sucesso.")
      print(f"Novo estoque de {produto}: {estoque[produto]} unidades.")
  else:
      print(f"Não foi possível realizar a entrega de {quantidade} unidades de {produdo}. Estoque insuficiente.")


# modulo 2 - Valmir

# modulo 3 - Samyra
def menu_mod3():
  print('''Escolha uma opção:
  1. Cadastrar Funcionário
  2. Gestão de Equipe
  3. Compartilhamento de Informações''')

def cadastro_funcionario():
  nome = input('Nome: ')
  cpf = input('CPF: ')
  idade = int(input('Idade: '))
  sexo = input('Sexo: ')
  while sexo not in 'MmFf':
    sexo = input('Dígito inválido! Tente novamente: ')
    if sexo in 'MmFf':
     continue
  cargo = input('Cargo: ')
  salario = float(input('Salário: '))
  historico_profissional = input('Histórico Profissional: ')
  area_acesso = input('Área de Acesso: ')
  with open('funcionarios.txt' , 'w') as func:
    func.write(f'{nome}, {idade}, {cpf}, {sexo}, {cargo}, {salario}, {historico_profissional}, {area_acesso}')
    print(func)
  try:
    with open('funcionarios.txt', 'w') as func:
      func.read()
      print(func)
  except FileNotFoundError as erro:
    print(f'ERRO: {erro}! Arquivo não encontrado. Tente novamente mais tarde!')
  funcionarios.append({'Nome': nome, 'CPF': cpf ,'Idade': idade, 'Sexo': sexo, 'Cargo': cargo, 'Salário': salario, 'Histórico Profissional': historico_profissional, 'Área de Acesso': area_acesso})
  print(funcionarios)

def gestao_equipe(): # escalas de trabalho, registro de horas e avaliações de desempenho dos funcionários
  nome = input('Nome: ')
  cargo = input('Cargo: ')
  print('''Escolha uma opção:
  1. Marcar Ponto
  2. Consultar Horas Trabalhadas
  3. Avaliação de Desempenho
  4. ENCERRAR''')
  opç = int(input('Opção: '))
  if opç == 1:
    data_ponto = input('Data da marcação do ponto [DD/MM/AAAA]: ')
    hora_ponto = input('Hora da marcação do ponto [HH:MM]: ')
    if data_ponto not in gestao:
      gestao[data_ponto] = hora_ponto
    else:
      gestao[data_ponto] += hora_ponto
    gestao.append({'Data do Ponto': data_ponto, 'Hora do Ponto': hora_ponto})
    print('PONTO REGISTRADO COM SUCESSO!')
  elif opç == 2:
    hora_trab = sum(gestao[hora_ponto.values()])
    print(f'Horas Trabalhadas: {hora_trab} horas')
    gestao.append({'Horas Trabalhadas': hora_trab})
  elif opç == 3:
    desempenho = int(input('Digite uma pontuação de 0 a 10 para o funcionário: '))
    while desempenho < 0 and desempenho > 10:
      desempenho = int(input('PONTUAÇÃO INVÁLIDA! Digite um número entre 0 e 10: '))
      if desempenho >= 0 and desempenho <= 10:
        break
    gestao.append({'Dempenho': desempenho})
    print('AVALIAÇÃO DE DESEMPENHO REGISTRADA COM SUCESSO!')
  elif opç == 4:
    print('ENCERRANDO...')
    break
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')

def partilha_informacoes(): # fazer que nem tipo o email
  contato = input('Com quem deseja entrar em contato? ')
  tema = input('Tema do contato: ')
  endereço = input('Digite o endereço de email: ')
  mensagem = input('Digite a mensagem: ')
  print(f'O {contato} irá receber a mesagem {mensagem} com o tema {tema}.')
  print('MENSAGEM ENVIADA COM SUCESSO! Aguarde o retorno do seu contato')

# modulo 4 - Valmir

# modulo 5 - Vitória

# modulo 6 - Vitória/Pedro

# chamada das funções (MAIN)
while True:
  menu()
  opcao = int(input('Opção: '))
  if opcao == 1:
    menu_mod1()
    opc_mod1 = int(input('Opção: '))
    if opc_mod1 == 1:
      controle_acesso()
    elif opc_mod1 == 2:
      monitora_estoque()
    elif opc_mod1 == 3:
      gera_alerta_estoque()
    elif opc_mod1 == 4:
      atualiza_estoque()
    else:
      print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')
      break
    print()
  elif opcao == 2:
    print()
  elif opcao == 3:
    menu_mod3()
    opc_mod3 = int(input('Opção: '))
    if opc_mod3 == 1:
      cadastro_funcionario()
    elif opc_mod3 == 2:
      gestao_equipe()
    elif opc_mod3 == 3:
      partilha_informacoes()
    else:
      print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')
      break
    print()
  elif opcao == 4:
    print()
  elif opcao == 5:
    print()
  elif opcao == 6:
    print()
  elif opcao == 7:
    print()
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente mais tarde.')

