import json

class SistemaRestaurante:
    def __init__(self):
        # Dados iniciais
        self.perfis_acesso = {}
        self.produtos = {}
        self.estoque = {}
        self.cardapios = {}

    def criar_perfil_acesso(self, funcionario, areas_permitidas):
        self.perfis_acesso[funcionario] = areas_permitidas
        print(f'Perfil de acesso criado para {funcionario}: {areas_permitidas}')

    def cadastrar_produto(self, produto, categoria, quantidade):
        self.produtos[produto] = {'categoria': categoria, 'quantidade': quantidade}
        print(f'Produto {produto} cadastrado na categoria {categoria} com quantidade {quantidade}')

    def monitorar_estoque(self):
        print("Estoque atual:")
        for produto, info in self.produtos.items():
            print(f'{produto}: {info["quantidade"]} unidades')

    def alertar_estoque_baixo(self, limite):
        print(f"Alertas de Estoque Baixo (limite: {limite}):")
        for produto, info in self.produtos.items():
            if info["quantidade"] < limite:
                print(f'Alerta: Estoque baixo para {produto}')

    def monitorar_producao(self):
        print("Monitorando a produção...")

    def cadastrar_cardapio(self, filial, pratos):
        self.cardapios[filial] = pratos
        print(f'Cardápio da filial {filial} cadastrado.')

    def exibir_cardapio(self, filial):
        print(f"Cardápio da filial {filial}:")
        for prato, info in self.cardapios.get(filial, {}).items():
            print(f'{prato}: {info["ingredientes"]} - R${info["preco"]}')

    def exibir_instrucoes_preparo(self, prato):
        print(f'Instruções de preparo para {prato}: {self.cardapios.get(prato, {}).get("instrucoes", "Não disponível")}')
    
    def salvar_dados(self, nome_arquivo='dados_restaurante.txt'):
        dados = {
            'perfis_acesso': self.perfis_acesso,
            'produtos': self.produtos,
            'cardapios': self.cardapios
        }

        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo)

    def carregar_dados(self, nome_arquivo='dados_restaurante.txt'):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                self.perfis_acesso = dados.get('perfis_acesso', {})
                self.produtos = dados.get('produtos', {})
                self.cardapios = dados.get('cardapios', {})
        except FileNotFoundError:
            print("Arquivo não encontrado. Usando dados padrão.")


# Exemplo de utilização interativa
sistema = SistemaRestaurante()
sistema.carregar_dados()  # Carrega dados do arquivo, se existir

while True:
    print("\n### Sistema de Restaurante ###")
    print("1. Criar Perfil de Acesso")
    print("2. Cadastrar Produto")
    print("3. Monitorar Estoque")
    print("4. Alertar Estoque Baixo")
    print("5. Monitorar Produção")
    print("6. Cadastrar Cardápio")
    print("7. Exibir Cardápio")
    print("8. Exibir Instruções de Preparo")
    print("9. Salvar Dados")
    print("0. Sair")

    escolha = input("Escolha uma opção (0-9): ")

    if escolha == '1':
        funcionario = input("Nome do funcionário: ")
        areas_permitidas = input("Áreas permitidas (separadas por vírgula): ").split(',')
        sistema.criar_perfil_acesso(funcionario, areas_permitidas)

    elif escolha == '2':
        produto = input("Nome do produto: ")
        categoria = input("Categoria do produto: ")
        quantidade = int(input("Quantidade do produto: "))
        sistema.cadastrar_produto(produto, categoria, quantidade)

    elif escolha == '3':
        sistema.monitorar_estoque()

    elif escolha == '4':
        limite = int(input("Informe o limite de estoque baixo: "))
        sistema.alertar_estoque_baixo(limite)

    elif escolha == '5':
        sistema.monitorar_producao()

    elif escolha == '6':
        filial = input("Nome da filial: ")
        pratos = {}
        while True:
            nome_prato = input("Nome do prato (ou 'sair' para encerrar): ")
            if nome_prato.lower() == 'sair':
                break
            ingredientes = input("Ingredientes do prato (separados por vírgula): ").split(',')
            preco = float(input("Preço do prato: "))
            instrucoes = input("Instruções de preparo: ")
            pratos[nome_prato] = {'ingredientes': ingredientes, 'preco': preco, 'instrucoes': instrucoes}
        sistema.cadastrar_cardapio(filial, pratos)

    elif escolha == '7':
        filial = input("Nome da filial: ")
        sistema.exibir_cardapio(filial)

    elif escolha == '8':
        prato = input("Nome do prato: ")
        sistema.exibir_instrucoes_preparo(prato)

    elif escolha == '9':
        sistema.salvar_dados()
        print("Dados salvos com sucesso!")

    elif escolha == '0':
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
